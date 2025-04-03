from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation
from aggregator_opengateway_sdk import QoDMobile, ClientCredentials, QoSProfiles


# Instantation of DeviceLocation class
credentials = ClientCredentials(
    clientid='4e25bbc6-db6f-4385-be96-69f0a049428e',
    clientsecret='4d2d3539-dfcb-4f92-b00c-fed81a46a705'
)

customer_phone_number = "+34666666666"

devicelocation_client = DeviceLocation(credentials=credentials, phone_number=customer_phone_number)

# Usage of the instance

# Use case: Disoriented person

frequented_locations = [
    (40.5150, -3.6640, 2), 
    (40.7128, -3.0060, 0.5),  
    (40.5074, -3.1278, 1),   
    (40.8566, -3.3522, 2)     
]

result = true

for [lat,long,acc] in frequented_locations: # Checking all the frequently visited locations
    if devicelocation_client.verify(lat,long,acc, customer_phone_number):
        result = false
        break 

print(f"Is the person disoriented or lost? {result}")


# Use case: Person in danger

# Here, time highly matters. We will try to get all the resources needed ASAP. For that,
# we use QoD.

# Instantation of QoDMobile class
credentials = ClientCredentials(
    clientid='4e25bbc6-db6f-4385-be96-69f0a049428e',
    clientsecret='4d2d3539-dfcb-4f92-b00c-fed81a46a705'
)

device_ip_address = self.get_device_ip()  # e.g. '203.0.113.25:8080'

qod_client = QoDMobile(client=credentials, ip_address=device_ip_address)

duration = 7200  # 2 hours
qod_client.set_quality(duration, QoSProfiles.QOS_E)

# now we check if the person is in a dangerous area
danger_location = [40.5170, -3.6670, 4]

result = devicelocation_client.verify(danger_location[0], danger_location[1], danger_location[2], customer_phone_number)  # as set in the authorization step

print(f"Is the person in danger? {result}")
