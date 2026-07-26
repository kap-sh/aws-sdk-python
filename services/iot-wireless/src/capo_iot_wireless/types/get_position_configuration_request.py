"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.position_resource_identifier
    import capo_iot_wireless.types.position_resource_type


class GetPositionConfigurationRequest(TypedDict, closed=True):
    resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>Resource identifier used in a position configuration.</p>"""
    resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType"
    """<p>Resource type of the resource for which position configuration is retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPositionConfigurationRequest:
    out: GetPositionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
