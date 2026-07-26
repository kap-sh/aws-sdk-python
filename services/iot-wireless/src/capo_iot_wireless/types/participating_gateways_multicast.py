"""Generated from Smithy shape ``com.amazonaws.iotwireless#ParticipatingGatewaysMulticast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.gateway_list_multicast
    import capo_iot_wireless.types.transmission_interval_multicast


class ParticipatingGatewaysMulticast(TypedDict, closed=True):
    gateway_list: NotRequired[
        "capo_iot_wireless.types.gateway_list_multicast.GatewayListMulticast"
    ]
    """<p>The list of gateways that you want to use for sending the multicast downlink message. Each downlink message will be sent to all the gateways in the list in the order that you provided. If the gateway list is empty, then AWS IoT Core for LoRaWAN chooses the gateways that were most recently used by the devices to send an uplink message.</p>"""
    transmission_interval: NotRequired[
        "capo_iot_wireless.types.transmission_interval_multicast.TransmissionIntervalMulticast"
    ]
    """<p>The duration of time in milliseconds for which AWS IoT Core for LoRaWAN will wait before transmitting the multicast payload to the next gateway in the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingGatewaysMulticast) -> dict:
    out: dict = {}
    if "gateway_list" in value:
        import capo_iot_wireless.types.gateway_list_multicast

        out["GatewayList"] = (
            capo_iot_wireless.types.gateway_list_multicast.serialize_json(
                value["gateway_list"]
            )
        )
    if "transmission_interval" in value:
        out["TransmissionInterval"] = value["transmission_interval"]
    return out


def deserialize_json(data: dict) -> ParticipatingGatewaysMulticast:
    out: ParticipatingGatewaysMulticast = {}  # type: ignore[typeddict-item]
    if "GatewayList" in data:
        import capo_iot_wireless.types.gateway_list_multicast

        out["gateway_list"] = (
            capo_iot_wireless.types.gateway_list_multicast.deserialize_json(
                data["GatewayList"]
            )
        )
    if "TransmissionInterval" in data:
        out["transmission_interval"] = data["TransmissionInterval"]
    return out
