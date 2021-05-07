import tldextract


def insert_all_indexes(domains: list, words: list) -> list:
    mutated_domains: list = []
    if domains:
        for domain in domains:
            domain_parts = tldextract.extract(domain.strip())
            domain_sub = domain_parts.subdomain.split(".")
            for word in words:
                for index in range(0, len(domain_sub)):
                    domain_sub.insert(index, word.strip())
                    actual_sub = ".".join(domain_sub)
                    full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                    if actual_sub[-1:] != ".":
                        mutated_domains.append(full_domain)
                    domain_sub.pop(index)
                domain_sub.append(word.strip())
                actual_sub = ".".join(domain_sub)
                full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                if len(domain_sub[0]) > 0:
                    mutated_domains.append(full_domain)
                domain_sub.pop()
    return mutated_domains


def insert_number_suffix(domains: list) -> list:
    mutated_domains: list = []
    if domains:
        for domain in domains:
            domain_parts = tldextract.extract(domain.strip())
            domain_sub = domain_parts.subdomain.split(".")
            for word in range(0, 10):
                for index, value in enumerate(domain_sub):
                    original_sub = domain_sub[index]
                    domain_sub[index] = domain_sub[index] + "-" + str(word)
                    actual_sub = ".".join(domain_sub)
                    full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                    mutated_domains.append(full_domain)
                    domain_sub[index] = original_sub

                    original_sub = domain_sub[index]
                    domain_sub[index] = domain_sub[index] + str(word)
                    actual_sub = ".".join(domain_sub)
                    full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                    mutated_domains.append(full_domain)
                    domain_sub[index] = original_sub
    return mutated_domains


def insert_dashes(domains: list, words: list) -> list:
    mutated_domains: list = []
    if domains:
        for domain in domains:
            domain_parts = tldextract.extract(domain.strip())
            domain_sub = domain_parts.subdomain.split(".")
            for word in words:
                for index, value in enumerate(domain_sub):
                    original_sub = domain_sub[index]
                    domain_sub[index] = domain_sub[index] + "-" + str(word).strip()
                    actual_sub = ".".join(domain_sub)
                    full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                    if len(domain_sub[0]) > 0 and domain_sub[:1] != "-":
                        mutated_domains.append(full_domain)
                    domain_sub[index] = original_sub
                    domain_sub[index] = str(word).strip() + "-" + domain_sub[index]
                    actual_sub = ".".join(domain_sub)
                    full_domain = f"{actual_sub}.{domain_parts.domain}.{domain_parts.suffix}"
                    if domain_sub[-1:] != "-":
                        mutated_domains.append(full_domain)
                    domain_sub[index] = original_sub
    return mutated_domains
