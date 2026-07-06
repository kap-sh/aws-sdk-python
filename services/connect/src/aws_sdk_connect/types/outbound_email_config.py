"""Generated from Smithy shape ``com.amazonaws.connect#OutboundEmailConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_id


class OutboundEmailConfig(TypedDict, closed=True):
    outbound_email_address_id: NotRequired[
        "aws_sdk_connect.types.email_address_id.EmailAddressId"
    ]
    """<p>The identifier of the email address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundEmailConfig) -> dict:
    out: dict = {}
    if "outbound_email_address_id" in value:
        out["OutboundEmailAddressId"] = value["outbound_email_address_id"]
    return out


def deserialize_json(data: dict) -> OutboundEmailConfig:
    out: OutboundEmailConfig = {}  # type: ignore[typeddict-item]
    if "OutboundEmailAddressId" in data:
        out["outbound_email_address_id"] = data["OutboundEmailAddressId"]
    return out
