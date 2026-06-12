"""Generated from Smithy shape ``com.amazonaws.iotwireless#ParticipatingGateways``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.downlink_mode
    import aws_sdk_iot_wireless.types.gateway_list
    import aws_sdk_iot_wireless.types.transmission_interval


class ParticipatingGateways(TypedDict):
    downlink_mode: "aws_sdk_iot_wireless.types.downlink_mode.DownlinkMode"
    """<p>Indicates whether to send the downlink message in sequential mode or concurrent mode, or to use only the chosen gateways from the previous uplink message transmission.</p>"""
    gateway_list: "aws_sdk_iot_wireless.types.gateway_list.GatewayList"
    """<p>The list of gateways that you want to use for sending the downlink data traffic.</p>"""
    transmission_interval: (
        "aws_sdk_iot_wireless.types.transmission_interval.TransmissionInterval"
    )
    """<p>The duration of time for which AWS IoT Core for LoRaWAN will wait before transmitting the payload to the next gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingGateways) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.downlink_mode

    out["DownlinkMode"] = aws_sdk_iot_wireless.types.downlink_mode.serialize_json(
        value["downlink_mode"]
    )
    import aws_sdk_iot_wireless.types.gateway_list

    out["GatewayList"] = aws_sdk_iot_wireless.types.gateway_list.serialize_json(
        value["gateway_list"]
    )
    out["TransmissionInterval"] = value["transmission_interval"]
    return out


def deserialize_json(data: dict) -> ParticipatingGateways:
    out: ParticipatingGateways = {}  # type: ignore[typeddict-item]
    if "DownlinkMode" in data:
        import aws_sdk_iot_wireless.types.downlink_mode

        out["downlink_mode"] = (
            aws_sdk_iot_wireless.types.downlink_mode.deserialize_json(
                data["DownlinkMode"]
            )
        )
    else:
        raise DeserializationError("ParticipatingGateways.downlink_mode required")
    if "GatewayList" in data:
        import aws_sdk_iot_wireless.types.gateway_list

        out["gateway_list"] = aws_sdk_iot_wireless.types.gateway_list.deserialize_json(
            data["GatewayList"]
        )
    else:
        raise DeserializationError("ParticipatingGateways.gateway_list required")
    if "TransmissionInterval" in data:
        out["transmission_interval"] = data["TransmissionInterval"]
    else:
        raise DeserializationError(
            "ParticipatingGateways.transmission_interval required"
        )
    return out
