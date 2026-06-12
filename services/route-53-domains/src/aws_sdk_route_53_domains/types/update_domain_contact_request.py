"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateDomainContactRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.consent
    import aws_sdk_route_53_domains.types.contact_detail
    import aws_sdk_route_53_domains.types.domain_name


class UpdateDomainContactRequest(TypedDict):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to update contact information for.</p>"""
    admin_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    registrant_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    tech_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    consent: NotRequired["aws_sdk_route_53_domains.types.consent.Consent"]
    """<p> Customer's consent for the owner change request. Required if the domain is not free (consent price is more than $0.00).</p>"""
    billing_contact: NotRequired[
        "aws_sdk_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainContactRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
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
    if "consent" in value:
        import aws_sdk_route_53_domains.types.consent

        out["Consent"] = aws_sdk_route_53_domains.types.consent.serialize_aws_json_1_1(
            value["consent"]
        )
    if "billing_contact" in value:
        import aws_sdk_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            aws_sdk_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["billing_contact"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDomainContactRequest:
    out: UpdateDomainContactRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("UpdateDomainContactRequest.domain_name required")
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
    if "Consent" in data:
        import aws_sdk_route_53_domains.types.consent

        out["consent"] = (
            aws_sdk_route_53_domains.types.consent.deserialize_aws_json_1_1(
                data["Consent"]
            )
        )
    if "BillingContact" in data:
        import aws_sdk_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            aws_sdk_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    return out
