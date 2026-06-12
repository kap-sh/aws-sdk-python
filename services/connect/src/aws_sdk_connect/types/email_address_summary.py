"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.email_address_arn
    import aws_sdk_connect.types.email_address_id


class EmailAddressSummary(TypedDict):
    id: NotRequired["aws_sdk_connect.types.email_address_id.EmailAddressId"]
    """<p>The unique identifier of the email address associated with the queue.</p>"""
    arn: NotRequired["aws_sdk_connect.types.email_address_arn.EmailAddressArn"]
    """<p>The Amazon Resource Name (ARN) of the email address associated with the queue.</p>"""
    is_default_outbound_email: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Indicates whether this email address is configured as the default outbound email address for the queue. When set to true, this email address is used as the default sender for outbound email contacts from this queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["IsDefaultOutboundEmail"] = value.get("is_default_outbound_email", False)
    return out


def deserialize_json(data: dict) -> EmailAddressSummary:
    out: EmailAddressSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "IsDefaultOutboundEmail" in data:
        out["is_default_outbound_email"] = data["IsDefaultOutboundEmail"]
    else:
        out["is_default_outbound_email"] = False
    return out
