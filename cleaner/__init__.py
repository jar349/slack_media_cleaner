from slackclient import SlackClient


class Cleaner(object):
    def __init__(self, config, args):
        self.config = config
        self.args = args
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
        max_pages = self.args.pages
        more_pages = True
        should_continue = True

        while more_pages and should_continue:
            more_pages, file_list = self.get_file_list_page(page=current_page)
            for file in file_list:
                if self.args.noop:
                    print "would have deleted: " + file['name'] + "(" + file['id'] + ")"
                else:
                    self.delete_file(file['id'])
            current_page+=1
            should_continue = current_page < max_pages if max_pages else True

        print "Done deleting images"

