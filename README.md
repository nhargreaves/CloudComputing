# CloudComputing
A docker/python project using a load generator which extracts json data on CPU utilisation via cAdvisor to a mongo database.

dist.py is a basic load generator accessing an image container which outputs time taken to calculate the prime of a random large integer. The load generator uses a poisson/normal distribution (depending on input) to calculate the time between requests.
getInfo.py uses cAdvisor statistics to extract the cpu and memory utilisation data of the web container and outputs this automatically into a mongo database. This allows the CPU spikes produced by the load generator's requests to be seen and tracked.
