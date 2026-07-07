"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANMulticast``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.dl_class
    import aws_sdk_iot_wireless.types.participating_gateways_multicast
    import aws_sdk_iot_wireless.types.supported_rf_region


class LoRaWANMulticast(TypedDict, closed=True):
    rf_region: NotRequired[
        "aws_sdk_iot_wireless.types.supported_rf_region.SupportedRfRegion"
    ]
    dl_class: NotRequired["aws_sdk_iot_wireless.types.dl_class.DlClass"]
    participating_gateways: NotRequired[
        "aws_sdk_iot_wireless.types.participating_gateways_multicast.ParticipatingGatewaysMulticast"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANMulticast) -> dict:
    out: dict = {}
    if "rf_region" in value:
        import aws_sdk_iot_wireless.types.supported_rf_region

        out["RfRegion"] = aws_sdk_iot_wireless.types.supported_rf_region.serialize_json(
            value["rf_region"]
        )
    if "dl_class" in value:
        import aws_sdk_iot_wireless.types.dl_class

        out["DlClass"] = aws_sdk_iot_wireless.types.dl_class.serialize_json(
            value["dl_class"]
        )
    if "participating_gateways" in value:
        import aws_sdk_iot_wireless.types.participating_gateways_multicast

        out["ParticipatingGateways"] = (
            aws_sdk_iot_wireless.types.participating_gateways_multicast.serialize_json(
                value["participating_gateways"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANMulticast:
    out: LoRaWANMulticast = {}  # type: ignore[typeddict-item]
    if "RfRegion" in data:
        import aws_sdk_iot_wireless.types.supported_rf_region

        out["rf_region"] = (
            aws_sdk_iot_wireless.types.supported_rf_region.deserialize_json(
                data["RfRegion"]
            )
        )
    if "DlClass" in data:
        import aws_sdk_iot_wireless.types.dl_class

        out["dl_class"] = aws_sdk_iot_wireless.types.dl_class.deserialize_json(
            data["DlClass"]
        )
    if "ParticipatingGateways" in data:
        import aws_sdk_iot_wireless.types.participating_gateways_multicast

        out["participating_gateways"] = (
            aws_sdk_iot_wireless.types.participating_gateways_multicast.deserialize_json(
                data["ParticipatingGateways"]
            )
        )
    return out
