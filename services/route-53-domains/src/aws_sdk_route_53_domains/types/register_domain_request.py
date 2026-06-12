"""Generated from Smithy shape ``com.amazonaws.route53domains#RegisterDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.boolean
    import aws_sdk_route_53_domains.types.contact_detail
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.duration_in_years
    import aws_sdk_route_53_domains.types.lang_code


class RegisterDomainRequest(TypedDict):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The domain name that you want to register. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html\">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>The domain name can contain only the following characters:</p> <ul> <li> <p>Letters a through z. Domain names are not case sensitive.</p> </li> <li> <p>Numbers 0 through 9.</p> </li> <li> <p>Hyphen (-). You can't specify a hyphen at the beginning or end of a label. </p> </li> <li> <p>Period (.) to separate the labels in the name, such as the <code>.</code> in <code>example.com</code>.</p> </li> </ul> <p>Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html\">Domains that You Can Register with Amazon Route 53</a>. For more information, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-idns\">Formatting Internationalized Domain Names</a>. </p>"""
    idn_lang_code: NotRequired["aws_sdk_route_53_domains.types.lang_code.LangCode"]
    """<p>Reserved for future use.</p>"""
    duration_in_years: (
        "aws_sdk_route_53_domains.types.duration_in_years.DurationInYears"
    )
    """<p>The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html\">Domains that You Can Register with Amazon Route 53</a> in the <i>Amazon Route 53 Developer Guide</i>.</p> <p>Default: 1</p>"""
    auto_renew: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Indicates whether the domain will be automatically renewed (<code>true</code>) or not (<code>false</code>). Auto renewal only takes effect after the account is charged.</p> <p>Default: <code>true</code> </p>"""
    admin_contact: "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information. For information about the values that you specify for each element, see <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html\">ContactDetail</a>.</p>"""
    registrant_contact: "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information. For information about the values that you specify for each element, see <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html\">ContactDetail</a>.</p>"""
    tech_contact: "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    """<p>Provides detailed contact information. For information about the values that you specify for each element, see <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html\">ContactDetail</a>.</p>"""
    privacy_protect_admin_contact: NotRequired[
        "aws_sdk_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    privacy_protect_registrant_contact: NotRequired[
        "aws_sdk_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (the domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    privacy_protect_tech_contact: NotRequired[
        "aws_sdk_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note> <p>Default: <code>true</code> </p>"""
    billing_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information. For information about the values that you specify for each element, see <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html\">ContactDetail</a>.</p>"""
    privacy_protect_billing_contact: NotRequired[
        "aws_sdk_route_53_domains.types.boolean.Boolean"
    ]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "idn_lang_code" in value:
        out["IdnLangCode"] = value["idn_lang_code"]
    out["DurationInYears"] = value["duration_in_years"]
    if "auto_renew" in value:
        out["AutoRenew"] = value["auto_renew"]
    import aws_sdk_route_53_domains.types.contact_detail

    out["AdminContact"] = (
        aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["admin_contact"]
        )
    )
    import aws_sdk_route_53_domains.types.contact_detail

    out["RegistrantContact"] = (
        aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["registrant_contact"]
        )
    )
    import aws_sdk_route_53_domains.types.contact_detail

    out["TechContact"] = (
        aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
            value["tech_contact"]
        )
    )
    if "privacy_protect_admin_contact" in value:
        out["PrivacyProtectAdminContact"] = value["privacy_protect_admin_contact"]
    if "privacy_protect_registrant_contact" in value:
        out["PrivacyProtectRegistrantContact"] = value[
            "privacy_protect_registrant_contact"
        ]
    if "privacy_protect_tech_contact" in value:
        out["PrivacyProtectTechContact"] = value["privacy_protect_tech_contact"]
    if "billing_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["billing_contact"]
            )
        )
    if "privacy_protect_billing_contact" in value:
        out["PrivacyProtectBillingContact"] = value["privacy_protect_billing_contact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDomainRequest:
    out: RegisterDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("RegisterDomainRequest.domain_name required")
    if "IdnLangCode" in data:
        out["idn_lang_code"] = data["IdnLangCode"]
    if "DurationInYears" in data:
        out["duration_in_years"] = data["DurationInYears"]
    else:
        raise DeserializationError("RegisterDomainRequest.duration_in_years required")
    if "AutoRenew" in data:
        out["auto_renew"] = data["AutoRenew"]
    if "AdminContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["admin_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["AdminContact"]
            )
        )
    else:
        raise DeserializationError("RegisterDomainRequest.admin_contact required")
    if "RegistrantContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["registrant_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["RegistrantContact"]
            )
        )
    else:
        raise DeserializationError("RegisterDomainRequest.registrant_contact required")
    if "TechContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["tech_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["TechContact"]
            )
        )
    else:
        raise DeserializationError("RegisterDomainRequest.tech_contact required")
    if "PrivacyProtectAdminContact" in data:
        out["privacy_protect_admin_contact"] = data["PrivacyProtectAdminContact"]
    if "PrivacyProtectRegistrantContact" in data:
        out["privacy_protect_registrant_contact"] = data[
            "PrivacyProtectRegistrantContact"
        ]
    if "PrivacyProtectTechContact" in data:
        out["privacy_protect_tech_contact"] = data["PrivacyProtectTechContact"]
    if "BillingContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    if "PrivacyProtectBillingContact" in data:
        out["privacy_protect_billing_contact"] = data["PrivacyProtectBillingContact"]
    return out
