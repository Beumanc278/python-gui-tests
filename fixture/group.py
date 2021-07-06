from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        group_list = [Group(name=node.text()) for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, group_name):
        self.open_group_editor()
        self.group_editor.window(auto_id='uxNewAddressButton').click()
        input = self.group_editor.window(class_name='Edit')
        input.set_text(group_name)
        input.type_keys('\n')
        self.close_group_editor()

    def delete_group(self, group: Group):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        group = list(filter(lambda x: x.text() == group.name, root.children()))[0]
        group.click()
        self.group_editor.window(auto_id='uxDeleteAddressButton').click()
        delete_window = self.app.application.window(title='Delete group')
        delete_window.window(auto_id='uxDeleteAllRadioButton').click()
        delete_window.window(auto_id='uxOKAddressButton').click()

    def open_group_editor(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.group_editor = self.app.application.window(title='Group editor')
        self.group_editor.wait('visible')

    def close_group_editor(self):
        self.group_editor.close()
