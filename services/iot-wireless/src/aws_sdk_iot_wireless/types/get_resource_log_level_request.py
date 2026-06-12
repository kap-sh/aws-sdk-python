"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetResourceLogLevelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.resource_identifier
    import aws_sdk_iot_wireless.types.resource_type


class GetResourceLogLevelRequest(TypedDict):
    resource_identifier: (
        "aws_sdk_iot_wireless.types.resource_identifier.ResourceIdentifier"
    )
    resource_type: "aws_sdk_iot_wireless.types.resource_type.ResourceType"
    """<p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceLogLevelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceLogLevelRequest:
    out: GetResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
    return out
