import random

from model.group import Group


def test_add_group(app):
    old_list = app.groups.get_group_list()
    group_name = 'test_group_' + str(random.choice(range(1, 100)))
    app.groups.add_new_group(Group(name=group_name))
    new_list = app.groups.get_group_list()
    old_list.append(Group(name=group_name))
    assert sorted(old_list, key=lambda x: x.name) == sorted(new_list, key=lambda x: x.name)