from slackclient import SlackClient


class Cleaner(object):
    def __init__(self, config):
        self.config = config
        self.slack_client = SlackClient(config['slack_token'])

    def delete_file(self, file):
        try:
            self.slack_client.api_call(
                "files.delete",
                file=file
            )
            print "Deleted file: '%s'" % file
        except Exception as ex:
            print "Cannot delete '%s' due to an exception: %s" % (file, ex.message)

    def get_file_list_page(self, page=1):
        """
        gets a page of image files.  returns a tuple whose first element is whether there are more pages and whose
        second element is the page of files.
        """
        try:
            result = self.slack_client.api_call(
                "files.list",
                page=page,
                types="images"
            )
            print "Found %s images.  Deleting..." % result['paging']['total']
            pages = result['paging']['pages']
            return (pages > page, result['files'])
        except Exception as ex:
            print "Cannot list files due to an expcetion: %s" % ex.message
            return (False, [])

    def clean(self):
        current_page = 1
        more_pages = True

        while more_pages:
            more_pages, file_list = self.get_file_list_page(page=current_page)
            for file in file_list:
                self.delete_file(file['id'])
            current_page+=1

        print "Done deleting images"

