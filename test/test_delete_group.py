import random

from model.group import Group


def test_delete_group(app):
    if len(app.groups.get_group_list()) == 1:
        group_name = 'test_group_' + str(random.choice(range(1, 100)))
        app.groups.add_new_group(Group(name=group_name))
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.delete_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list, key=lambda x: x.name) == sorted(new_list, key=lambda x: x.name)
