"""Generated from Smithy shape ``com.amazonaws.route53domains#ResendContactReachabilityEmailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.boolean
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.email


class ResendContactReachabilityEmailResponse(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_route_53_domains.types.domain_name.DomainName"]
    """<p>The domain name for which you requested a confirmation email.</p>"""
    email_address: NotRequired["aws_sdk_route_53_domains.types.email.Email"]
    """<p>The email address for the registrant contact at the time that we sent the verification email.</p>"""
    is_already_verified: NotRequired["aws_sdk_route_53_domains.types.boolean.Boolean"]
    """<p> <code>True</code> if the email address for the registrant contact has already been verified, and <code>false</code> otherwise. If the email address has already been verified, we don't send another confirmation email.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResendContactReachabilityEmailResponse) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "is_already_verified" in value:
        out["isAlreadyVerified"] = value["is_already_verified"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResendContactReachabilityEmailResponse:
    out: ResendContactReachabilityEmailResponse = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    if "isAlreadyVerified" in data:
        out["is_already_verified"] = data["isAlreadyVerified"]
    return out
