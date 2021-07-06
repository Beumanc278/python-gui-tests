import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application('C:\\Users\\dmitriy.anurin\\Desktop\\AddressBook-for-test\\AddressBook.exe')
    request.addfinalizer(fixture.destroy)
    return fixture