"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.position_resource_identifier
    import aws_sdk_iot_wireless.types.position_resource_type


class GetPositionRequest(TypedDict):
    resource_identifier: "aws_sdk_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier"
    """<p>Resource identifier used to retrieve the position information.</p>"""
    resource_type: (
        "aws_sdk_iot_wireless.types.position_resource_type.PositionResourceType"
    )
    """<p>Resource type of the resource for which position information is retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPositionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPositionRequest:
    out: GetPositionRequest = {}  # type: ignore[typeddict-item]
    return out
