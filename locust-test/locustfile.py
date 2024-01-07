from locust import HttpUser, between, task


class mapServiceTest(HttpUser):
    wait_time = between(1, 5) # random wait time(1 to 5 seconds) between each task

        
    @task
    def map_get(self):
        self.client.get("/api/v1/clinics")

    @task
    def patient_get(self):
        self.client.get("/api/v1/patients/")

    @task
    def dentist_get(self):
        self.client.get("/api/v1/bookings/")

    # @task
    # def dentist_get(self):
    #     self.client.get("/api/v1/dentists/")
    

