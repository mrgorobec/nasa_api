def custom_assert_json(expected, actual):
    for _ in range(10):
        for x in expected['photos'][_].keys():
            assert expected['photos'][_][x] == actual['photos'][_][x]