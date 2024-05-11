class TextPost():
    def __init__(self, user, type, info):
        self.type = type
        self.info = info
        self.user = user

    def __str__(self):
        return self.user.name + " published a post:\n" + '"' + self.info + '"\n'
