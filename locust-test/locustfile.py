from locust import HttpUser, between, task


class mapServiceTest(HttpUser):
    wait_time = between(1, 5)

        
    @task
    def map_get(self):
        self.client.get("/api/v1/clinics")

    @task
    def patient_get(self):
        self.client.get("/api/v1/patients/")

    # @task
    # def dentist_get(self):
    #     self.client.get("/api/v1/dentists/")
    
    @task
    def dentist_get(self):
        self.client.get("/api/v1/bookings/")

    # ##map service
    # @task
    # def map_post(self):
    #     self.client.post("/api/v1/clinics",json={
    #       "clinicName":"Lindholmen Dental Clinic",
    #         "address": "Lindholmsplatsen 1",
    #          "dentistId": "TEST ID",
    #           "clinicEmail": "lindholmen@gmail.com"
    # })
    # @task
    # def map_patch(self):
    #     self.client.patch("/api/v1/clinics",json={
    #     "address": "Östra Hamngatan 32"
    # })
    
#     def on_start(self):
#         self.client.post("/api/v1/clinics",{
#     "clinicName":"Lindholmen Dental Clinic",
#     "address": "Lindholmsplatsen 1",
#     "dentistId": "TEST ID"
# })
    

    # @task
    # def userservice(self):
    #     self.client.post("/api/v1/patients/",json={
    #     "first_name": "azepei",
    #     "last_name": "azhao",
    #     "email": "a123@gmail.com",
    #     "password": "a123",
    #     "phone_number": 112234546464
    # })
        
    # @task
    # def get(self):
    #     self.client.get("/api/v1/patients/")
        

    # @task
    # def about(self):
    #     self.client.get("/about/")

