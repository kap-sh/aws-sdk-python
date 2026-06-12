"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityMailFromDomainAttributesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.mail_from_domain_attributes


class GetIdentityMailFromDomainAttributesResponse(TypedDict):
    mail_from_domain_attributes: (
        "aws_sdk_ses.types.mail_from_domain_attributes.MailFromDomainAttributes"
    )
    """<p>A map of identities to custom MAIL FROM attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityMailFromDomainAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.mail_from_domain_attributes

    aws_sdk_ses.types.mail_from_domain_attributes.serialize_query(
        value["mail_from_domain_attributes"],
        pairs,
        f"{prefix}.MailFromDomainAttributes",
    )


def deserialize_query(el: Element) -> GetIdentityMailFromDomainAttributesResponse:
    out: GetIdentityMailFromDomainAttributesResponse = {}  # type: ignore[typeddict-item]
    child_mail_from_domain_attributes = el.find("MailFromDomainAttributes")
    if child_mail_from_domain_attributes is not None:
        import aws_sdk_ses.types.mail_from_domain_attributes

        out["mail_from_domain_attributes"] = (
            aws_sdk_ses.types.mail_from_domain_attributes.deserialize_query(
                child_mail_from_domain_attributes
            )
        )
    else:
        raise DeserializationError(
            "GetIdentityMailFromDomainAttributesResponse.mail_from_domain_attributes required"
        )
    return out
