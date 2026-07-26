"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourcePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_resource_identifier
    import capo_iot_wireless.types.position_resource_type


class GetResourcePositionRequest(TypedDict, closed=True):
    resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>"""
    resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType"
    """<p>The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePositionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourcePositionRequest:
    out: GetResourcePositionRequest = {}  # type: ignore[typeddict-item]
    return out
