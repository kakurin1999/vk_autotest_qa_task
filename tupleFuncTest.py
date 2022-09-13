import pytest

#first test
def test_tuple_append_negative():
    try:
        assert (1,2,3,4,5).append(6)
    except AttributeError:
        pass

#second test
@pytest.mark.parametrize("tuple1,i,expected",
                         [
                        ((1,2,5),5,True),
                        ((1,4,5),2,False),
                        (tuple(),3,False)
                        ])

def test_tuple_including(tuple1,i,expected):
    assert (i in tuple1) == expected

def test_tuple_generator():
    a = 'priv'
    assert tuple(a) == ('p','r','i','v')
    a = 'kot'
    assert tuple(a) == ('k','o','t')
    a = 'sobaka'
    assert tuple(a) == ('s','o','b','a','k','a')
    a = ''
    assert tuple(a) == ()