"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANSendDataToDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.f_port
    import capo_iot_wireless.types.participating_gateways


class LoRaWANSendDataToDevice(TypedDict, closed=True):
    f_port: NotRequired["capo_iot_wireless.types.f_port.FPort"]
    participating_gateways: NotRequired[
        "capo_iot_wireless.types.participating_gateways.ParticipatingGateways"
    ]
    """<p>Choose the gateways that you want to use for the downlink data traffic when the wireless device is running in class B or class C mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANSendDataToDevice) -> dict:
    out: dict = {}
    if "f_port" in value:
        out["FPort"] = value["f_port"]
    if "participating_gateways" in value:
        import capo_iot_wireless.types.participating_gateways

        out["ParticipatingGateways"] = (
            capo_iot_wireless.types.participating_gateways.serialize_json(
                value["participating_gateways"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANSendDataToDevice:
    out: LoRaWANSendDataToDevice = {}  # type: ignore[typeddict-item]
    if "FPort" in data:
        out["f_port"] = data["FPort"]
    if "ParticipatingGateways" in data:
        import capo_iot_wireless.types.participating_gateways

        out["participating_gateways"] = (
            capo_iot_wireless.types.participating_gateways.deserialize_json(
                data["ParticipatingGateways"]
            )
        )
    return out
