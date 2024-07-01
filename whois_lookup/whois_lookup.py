import whois

domain = input("Enter domain name or IP address: ")

result = whois.whois(domain)

print("Domain name:", result.domain_name)
print("IP address:", result.query)
print("Registrar:", result.registrar)
print("Creation date:", result.creation_date)
print("Expiration date:", result.expiration_date)
print("Last updated:", result.last_updated)
print("Name servers:", result.name_servers)
