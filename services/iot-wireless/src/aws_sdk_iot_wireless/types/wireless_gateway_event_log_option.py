"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEventLogOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.log_level
    import aws_sdk_iot_wireless.types.wireless_gateway_event


class WirelessGatewayEventLogOption(TypedDict, closed=True):
    event: "aws_sdk_iot_wireless.types.wireless_gateway_event.WirelessGatewayEvent"
    log_level: "aws_sdk_iot_wireless.types.log_level.LogLevel"


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayEventLogOption) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.wireless_gateway_event

    out["Event"] = aws_sdk_iot_wireless.types.wireless_gateway_event.serialize_json(
        value["event"]
    )
    import aws_sdk_iot_wireless.types.log_level

    out["LogLevel"] = aws_sdk_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    return out


def deserialize_json(data: dict) -> WirelessGatewayEventLogOption:
    out: WirelessGatewayEventLogOption = {}  # type: ignore[typeddict-item]
    if "Event" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_event

        out["event"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_event.deserialize_json(
                data["Event"]
            )
        )
    else:
        raise DeserializationError("WirelessGatewayEventLogOption.event required")
    if "LogLevel" in data:
        import aws_sdk_iot_wireless.types.log_level

        out["log_level"] = aws_sdk_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        raise DeserializationError("WirelessGatewayEventLogOption.log_level required")
    return out
