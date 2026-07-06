"""Generated from Smithy shape ``com.amazonaws.iotwireless#PutResourceLogLevelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.resource_identifier
    import aws_sdk_iot_wireless.types.resource_type


class PutResourceLogLevelRequest(TypedDict, closed=True):
    resource_identifier: (
        "aws_sdk_iot_wireless.types.resource_identifier.ResourceIdentifier"
    )
    resource_type: "aws_sdk_iot_wireless.types.resource_type.ResourceType"
    """<p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>"""
    log_level: "aws_sdk_iot_wireless.types.log_level.LogLevel"


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceLogLevelRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.log_level

    out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    return out


def deserialize_json(data: dict) -> PutResourceLogLevelRequest:
    out: PutResourceLogLevelRequest = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        raise DeserializationError("PutResourceLogLevelRequest.log_level required")
    return out
