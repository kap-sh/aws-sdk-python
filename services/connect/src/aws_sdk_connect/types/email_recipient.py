"""Generated from Smithy shape ``com.amazonaws.connect#EmailRecipient``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.endpoint_address
    import aws_sdk_connect.types.endpoint_display_name


class EmailRecipient(TypedDict, closed=True):
    address: NotRequired["aws_sdk_connect.types.endpoint_address.EndpointAddress"]
    """<p>Address of the email recipient.</p>"""
    display_name: NotRequired[
        "aws_sdk_connect.types.endpoint_display_name.EndpointDisplayName"
    ]
    """<p>Display name of the email recipient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailRecipient) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> EmailRecipient:
    out: EmailRecipient = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
