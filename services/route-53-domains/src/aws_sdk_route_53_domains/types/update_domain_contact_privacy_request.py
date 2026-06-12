"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateDomainContactPrivacyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.boolean
    import aws_sdk_route_53_domains.types.domain_name


class UpdateDomainContactPrivacyRequest(TypedDict):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to update the privacy setting for.</p>"""
    admin_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the admin contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""
    registrant_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the registrant contact (domain owner).</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""
    tech_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p>Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the technical contact.</p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""
    billing_privacy: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p> Whether you want to conceal contact information from WHOIS queries. If you specify <code>true</code>, WHOIS (\"who is\") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify <code>false</code>, WHOIS queries return the information that you entered for the billing contact. </p> <note> <p>You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainContactPrivacyRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "admin_privacy" in value:
        out["AdminPrivacy"] = value["admin_privacy"]
    if "registrant_privacy" in value:
        out["RegistrantPrivacy"] = value["registrant_privacy"]
    if "tech_privacy" in value:
        out["TechPrivacy"] = value["tech_privacy"]
    if "billing_privacy" in value:
        out["BillingPrivacy"] = value["billing_privacy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDomainContactPrivacyRequest:
    out: UpdateDomainContactPrivacyRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "UpdateDomainContactPrivacyRequest.domain_name required"
        )
    if "AdminPrivacy" in data:
        out["admin_privacy"] = data["AdminPrivacy"]
    if "RegistrantPrivacy" in data:
        out["registrant_privacy"] = data["RegistrantPrivacy"]
    if "TechPrivacy" in data:
        out["tech_privacy"] = data["TechPrivacy"]
    if "BillingPrivacy" in data:
        out["billing_privacy"] = data["BillingPrivacy"]
    return out
