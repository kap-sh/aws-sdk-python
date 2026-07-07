"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class AssociateLinkRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "aws_sdk_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: "aws_sdk_networkmanager.types.link_id.LinkId"
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLinkRequest) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateLinkRequest:
    out: AssociateLinkRequest = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("AssociateLinkRequest.device_id required")
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    else:
        raise DeserializationError("AssociateLinkRequest.link_id required")
    return out
