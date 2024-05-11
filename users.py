from Followers import Followers
from posts import posts


class users(Followers):
    def __init__(self, name, password):
        super().__init__()
        self.name = name
        self.password = password
        self.status = False
        self.post = []
        self.notifications = []

    def set_status(self):
        self.status = not self.status

    def follow(self, user1):
        if self not in user1.followers and self != user1:
            user1.add_follower(self)
            print(self.name + " started following " + user1.name)

    def unfollow(self, user1):
        if self in user1.followers and self != user1:
            user1.remove_follower(self)
            print(self.name + " unfollowed " + user1.name)

    def publish_post(self, type, info, price=None, place=None):
        if type == "Text" or type == "Image" or type == "Sale":
            post1 = posts(self, type, info, price, place)
            print(post1)
            self.post.append(post1)
            self.notify_follower(self.name + " has a new post")
            return post1
        else:
            print("Invalid post type:", type)
            return None

    def print_notifications(self):
        print(self.name + "'s notifications:")
        for notification in self.notifications:
            print(notification)

    def add_notifications(self, notif):
        self.notifications.append(notif)

    def __str__(self):
        return "User name: " + self.name + ", Number of posts: " + str(
            len(self.post)) + ", Number of followers: " + str(len(self.followers))
