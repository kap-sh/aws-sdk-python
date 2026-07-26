"""Generated from Smithy shape ``com.amazonaws.route53domains#UpdateDomainContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53_domains.types.consent
    import capo_route_53_domains.types.contact_detail
    import capo_route_53_domains.types.domain_name


class UpdateDomainContactRequest(TypedDict, closed=True):
    domain_name: "capo_route_53_domains.types.domain_name.DomainName"
    """<p>The name of the domain that you want to update contact information for.</p>"""
    admin_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    registrant_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    tech_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""
    consent: NotRequired["capo_route_53_domains.types.consent.Consent"]
    """<p> Customer's consent for the owner change request. Required if the domain is not free (consent price is more than $0.00).</p>"""
    billing_contact: NotRequired[
        "capo_route_53_domains.types.contact_detail.ContactDetail"
    ]
    """<p>Provides detailed contact information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainContactRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "admin_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["AdminContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["admin_contact"]
            )
        )
    if "registrant_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["RegistrantContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["registrant_contact"]
            )
        )
    if "tech_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["TechContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
                value["tech_contact"]
            )
        )
    if "consent" in value:
        import capo_route_53_domains.types.consent

        out["Consent"] = capo_route_53_domains.types.consent.serialize_aws_json_1_1(
            value["consent"]
        )
    if "billing_contact" in value:
        import capo_route_53_domains.types.contact_detail

        out["BillingContact"] = (
            capo_route_53_domains.types.contact_detail.serialize_aws_json_1_1(
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
        import capo_route_53_domains.types.contact_detail

        out["admin_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["AdminContact"]
            )
        )
    if "RegistrantContact" in data:
        import capo_route_53_domains.types.contact_detail

        out["registrant_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["RegistrantContact"]
            )
        )
    if "TechContact" in data:
        import capo_route_53_domains.types.contact_detail

        out["tech_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["TechContact"]
            )
        )
    if "Consent" in data:
        import capo_route_53_domains.types.consent

        out["consent"] = capo_route_53_domains.types.consent.deserialize_aws_json_1_1(
            data["Consent"]
        )
    if "BillingContact" in data:
        import capo_route_53_domains.types.contact_detail

        out["billing_contact"] = (
            capo_route_53_domains.types.contact_detail.deserialize_aws_json_1_1(
                data["BillingContact"]
            )
        )
    return out
