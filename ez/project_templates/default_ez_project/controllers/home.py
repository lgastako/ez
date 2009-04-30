import ez


def index(request):
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    return ez.render(locals())
