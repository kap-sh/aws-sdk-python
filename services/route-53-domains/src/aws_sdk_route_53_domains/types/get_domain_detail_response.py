"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainDetailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.boolean
    import aws_sdk_route_53_domains.types.contact_detail
    import aws_sdk_route_53_domains.types.contact_number
    import aws_sdk_route_53_domains.types.dns_sec
    import aws_sdk_route_53_domains.types.dnssec_key_list
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.domain_status_list
    import aws_sdk_route_53_domains.types.email
    import aws_sdk_route_53_domains.types.nameserver_list
    import aws_sdk_route_53_domains.types.registrar_name
    import aws_sdk_route_53_domains.types.registrar_url
    import aws_sdk_route_53_domains.types.registrar_who_is_server
    import aws_sdk_route_53_domains.types.registry_domain_id
    import aws_sdk_route_53_domains.types.reseller
    import aws_sdk_route_53_domains.types.timestamp


class GetDomainDetailResponse(TypedDict):
    domain_name: NotRequired["aws_sdk_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of a domain.</p>"""
    nameservers: NotRequired[
        "aws_sdk_route_53_domains.types.nameserver_list.NameserverList"
    ]
    """<p>The name servers of the domain.</p>"""
    auto_renew: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether the domain registration is set to renew automatically.</p>"""
    admin_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain administrative contact.</p>"""
    registrant_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain registrant.</p>"""
    tech_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain technical contact.</p>"""
    admin_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p>"""
    registrant_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p>"""
    tech_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p>"""
    registrar_name: NotRequired[
        "aws_sdk_route_53_domains.types.registrar_name.RegistrarName"
    ]
    """<p>Name of the registrar of the domain as identified in the registry. </p>"""
    who_is_server: NotRequired[
        "aws_sdk_route_53_domains.types.registrar_who_is_server.RegistrarWhoIsServer"
    ]
    """<p>The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.</p>"""
    registrar_url: NotRequired[
        "aws_sdk_route_53_domains.types.registrar_url.RegistrarUrl"
    ]
    """<p>Web address of the registrar.</p>"""
    abuse_contact_email: NotRequired["aws_sdk_route_53_domains.types.email.Email"]
    """<p>Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.</p>"""
    abuse_contact_phone: NotRequired[
        "aws_sdk_route_53_domains.types.contact_number.ContactNumber"
    ]
    """<p>Phone number for reporting abuse.</p>"""
    registry_domain_id: NotRequired[
        "aws_sdk_route_53_domains.types.registry_domain_id.RegistryDomainId"
    ]
    """<p>Reserved for future use.</p>"""
    creation_date: NotRequired["aws_sdk_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date when the domain was created as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    updated_date: NotRequired["aws_sdk_route_53_domains.types.timestamp.Timestamp"]
    """<p>The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    expiration_date: NotRequired["aws_sdk_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date when the registration for the domain is set to expire. The date and time is in Unix time format and Coordinated Universal time (UTC).</p>"""
    reseller: NotRequired["aws_sdk_route_53_domains.types.reseller.Reseller"]
    """<p>Reserved for future use.</p>"""
    dns_sec: NotRequired["aws_sdk_route_53_domains.types.dns_sec.DNSSec"]
    """<p>Deprecated.</p>"""
    status_list: NotRequired[
        "aws_sdk_route_53_domains.types.domain_status_list.DomainStatusList"
    ]
    """<p>An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.</p> <p>ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.</p> <p>For a current list of domain name status codes and an explanation of what each code means, go to the <a href=\"https://www.icann.org/\">ICANN website</a> and search for <code>epp status codes</code>. (Search on the ICANN website; web searches sometimes return an old version of the document.)</p>"""
    dnssec_keys: NotRequired[
        "aws_sdk_route_53_domains.types.dnssec_key_list.DnssecKeyList"
    ]
    """<p>A complex type that contains information about the DNSSEC configuration.</p>"""
    billing_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides details about the domain billing contact.</p>"""
    billing_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Specifies whether contact information is concealed from WHOIS queries. If the value is <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is <code>false</code>, WHOIS queries return the information that you entered for the billing contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainDetailResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "nameservers" in value:
        import aws_sdk_route_53_domains.types.nameserver_list

        out["Nameservers"] = (
            aws_sdk_route_53_domains.types.nameserver_list.serialize_aws_json_1_1(
                value["nameservers"]
            )
        )
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    if "admin_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["AdminContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["admin_contact"]
            )
        )
    if "registrant_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["RegistrantContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["registrant_contact"]
            )
        )
    if "tech_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["TechContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["tech_contact"]
            )
        )
    if "admin_privacy" in value:
        out["AdminPrivacy"] = value["admin_privacy"]
    if "registrant_privacy" in value:
        out["RegistrantPrivacy"] = value["registrant_privacy"]
    if "tech_privacy" in value:
        out["TechPrivacy"] = value["tech_privacy"]
    if "registrar_name" in value:
        out["RegistrarName"] = value["registrar_name"]
    if "who_is_server" in value:
        out["WhoIsServer"] = value["who_is_server"]
    if "registrar_url" in value:
        out["RegistrarUrl"] = value["registrar_url"]
    if "abuse_contact_email" in value:
        out["AbuseContactEmail"] = value["abuse_contact_email"]
    if "abuse_contact_phone" in value:
        out["AbuseContactPhone"] = value["abuse_contact_phone"]
    if "registry_domain_id" in value:
        out["RegistryDomainId"] = value["registry_domain_id"]
    if "creation_date" in value:
        import aws_sdk_route_53_domains.types.timestamp

        out["CreationDate"] = (
            aws_sdk_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "updated_date" in value:
        import aws_sdk_route_53_domains.types.timestamp

        out["UpdatedDate"] = (
            aws_sdk_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["updated_date"]
            )
        )
    if "expiration_date" in value:
        import aws_sdk_route_53_domains.types.timestamp

        out["ExpirationDate"] = (
            aws_sdk_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["expiration_date"]
            )
        )
    if "reseller" in value:
        out["Reseller"] = value["reseller"]
    if "dns_sec" in value:
        out["DnsSec"] = value["dns_sec"]
    if "status_list" in value:
        import aws_sdk_route_53_domains.types.domain_status_list

        out["StatusList"] = (
            aws_sdk_route_53_domains.types.domain_status_list.serialize_aws_json_1_1(
                value["status_list"]
            )
        )
    if "dnssec_keys" in value:
        import aws_sdk_route_53_domains.types.dnssec_key_list

        out["DnssecKeys"] = (
            aws_sdk_route_53_domains.types.dnssec_key_list.serialize_aws_json_1_1(
                value["dnssec_keys"]
            )
        )
    if "billing_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["billing_contact"]
            )
        )
    if "billing_privacy" in value:
        out["BillingPrivacy"] = value["billing_privacy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainDetailResponse:
    out: GetDomainDetailResponse = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "Nameservers" in data:
        import aws_sdk_route_53_domains.types.nameserver_list

        out["nameservers"] = (
            aws_sdk_route_53_domains.types.nameserver_list.deserialize_aws_json_1_1(
                data["Nameservers"]
            )
        )
    if "AutoRenew" in data:
        out["auto_renew"] = data["AutoRenew"]
    if "AdminContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["admin_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["AdminContact"]
            )
        )
    if "RegistrantContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["registrant_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["RegistrantContact"]
            )
        )
    if "TechContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["tech_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["TechContact"]
            )
        )
    if "AdminPrivacy" in data:
        out["admin_privacy"] = data["AdminPrivacy"]
    if "RegistrantPrivacy" in data:
        out["registrant_privacy"] = data["RegistrantPrivacy"]
    if "TechPrivacy" in data:
        out["tech_privacy"] = data["TechPrivacy"]
    if "RegistrarName" in data:
        out["registrar_name"] = data["RegistrarName"]
    if "WhoIsServer" in data:
        out["who_is_server"] = data["WhoIsServer"]
    if "RegistrarUrl" in data:
        out["registrar_url"] = data["RegistrarUrl"]
    if "AbuseContactEmail" in data:
        out["abuse_contact_email"] = data["AbuseContactEmail"]
    if "AbuseContactPhone" in data:
        out["abuse_contact_phone"] = data["AbuseContactPhone"]
    if "RegistryDomainId" in data:
        out["registry_domain_id"] = data["RegistryDomainId"]
    if "CreationDate" in data:
        import aws_sdk_route_53_domains.types.timestamp

        out["creation_date"] = (
            aws_sdk_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "UpdatedDate" in data:
        import aws_sdk_route_53_domains.types.timestamp

        out["updated_date"] = (
            aws_sdk_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["UpdatedDate"]
            )
        )
    if "ExpirationDate" in data:
        import aws_sdk_route_53_domains.types.timestamp

        out["expiration_date"] = (
            aws_sdk_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationDate"]
            )
        )
    if "Reseller" in data:
        out["reseller"] = data["Reseller"]
    if "DnsSec" in data:
        out["dns_sec"] = data["DnsSec"]
    if "StatusList" in data:
        import aws_sdk_route_53_domains.types.domain_status_list

        out["status_list"] = (
            aws_sdk_route_53_domains.types.domain_status_list.deserialize_aws_json_1_1(
                data["StatusList"]
            )
        )
    if "DnssecKeys" in data:
        import aws_sdk_route_53_domains.types.dnssec_key_list

        out["dnssec_keys"] = (
            aws_sdk_route_53_domains.types.dnssec_key_list.deserialize_aws_json_1_1(
                data["DnssecKeys"]
            )
        )
    if "BillingContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    if "BillingPrivacy" in data:
        out["billing_privacy"] = data["BillingPrivacy"]
    return out
