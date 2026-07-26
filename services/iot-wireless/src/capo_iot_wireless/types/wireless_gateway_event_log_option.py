"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEventLogOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.wireless_gateway_event


class WirelessGatewayEventLogOption(TypedDict, closed=True):
    event: "capo_iot_wireless.types.wireless_gateway_event.WirelessGatewayEvent"
    log_level: "capo_iot_wireless.types.log_level.LogLevel"


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayEventLogOption) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.wireless_gateway_event

    out["Event"] = capo_iot_wireless.types.wireless_gateway_event.serialize_json(
        value["event"]
    )
    import capo_iot_wireless.types.log_level

    out["LogLevel"] = capo_iot_wireless.types.log_level.serialize_json(
        value["log_level"]
    )
    return out


def deserialize_json(data: dict) -> WirelessGatewayEventLogOption:
    out: WirelessGatewayEventLogOption = {}  # type: ignore[typeddict-item]
    if "Event" in data:
        import capo_iot_wireless.types.wireless_gateway_event

        out["event"] = capo_iot_wireless.types.wireless_gateway_event.deserialize_json(
            data["Event"]
        )
    else:
        raise DeserializationError("WirelessGatewayEventLogOption.event required")
    if "LogLevel" in data:
        import capo_iot_wireless.types.log_level

        out["log_level"] = capo_iot_wireless.types.log_level.deserialize_json(
            data["LogLevel"]
        )
    else:
        raise DeserializationError("WirelessGatewayEventLogOption.log_level required")
    return out
