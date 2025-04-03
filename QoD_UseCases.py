from aggregator_opengateway_sdk import QoDMobile, ClientCredentials, QoSProfiles

# Instantation of QoDMobile class
credentials = ClientCredentials(
    clientid='4e25bbc6-db6f-4385-be96-69f0a049428e',
    clientsecret='4d2d3539-dfcb-4f92-b00c-fed81a46a705'
)

device_ip_address = self.get_device_ip()  # e.g. '203.0.113.25:8080'


qod_client = QoDMobile(client=credentials, ip_address=device_ip_address)
# Note that, for each use case, we should have one different instance of qod_client
# Since we are implementing a mock app, we will use the same IP for all of them

# Usage of the instance

# Use case: White cane (Visually impaired people)
duration = 5400  # 1 hour 30 minutes
qod_client.set_quality(duration, QoSProfiles.QOS_L)

# Use case: Audio transcript (Hearing impaired people)
duration = 7200  # 2 hours
qod_client.set_quality(duration, QoSProfiles.QOS_L)

# Use case: Showleap, Iris recognition (Reduced mobility people)
duration = 7200  # 2 hours
qod_client.set_quality(duration, QoSProfiles.QOS_S)
