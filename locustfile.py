from locust import HttpUser, task, between


class MyWebsiteUser(HttpUser):

    @task
    def load_site(self):
        self.client.get("/")

    wait_time = between(1, 2)

