"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANUpdateGatewayTaskCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.crc
    import capo_iot_wireless.types.lo_ra_wan_gateway_version
    import capo_iot_wireless.types.update_signature


class LoRaWANUpdateGatewayTaskCreate(TypedDict, closed=True):
    update_signature: NotRequired[
        "capo_iot_wireless.types.update_signature.UpdateSignature"
    ]
    """<p>The signature used to verify the update firmware.</p>"""
    sig_key_crc: NotRequired["capo_iot_wireless.types.crc.Crc"]
    """<p>The CRC of the signature private key to check.</p>"""
    current_version: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The version of the gateways that should receive the update.</p>"""
    update_version: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The firmware version to update the gateway to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANUpdateGatewayTaskCreate) -> dict:
    out: dict = {}
    if "update_signature" in value:
        out["UpdateSignature"] = value["update_signature"]
    if "sig_key_crc" in value:
        out["SigKeyCrc"] = value["sig_key_crc"]
    if "current_version" in value:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["CurrentVersion"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.serialize_json(
                value["current_version"]
            )
        )
    if "update_version" in value:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["UpdateVersion"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.serialize_json(
                value["update_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANUpdateGatewayTaskCreate:
    out: LoRaWANUpdateGatewayTaskCreate = {}  # type: ignore[typeddict-item]
    if "UpdateSignature" in data:
        out["update_signature"] = data["UpdateSignature"]
    if "SigKeyCrc" in data:
        out["sig_key_crc"] = data["SigKeyCrc"]
    if "CurrentVersion" in data:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["current_version"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.deserialize_json(
                data["CurrentVersion"]
            )
        )
    if "UpdateVersion" in data:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["update_version"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.deserialize_json(
                data["UpdateVersion"]
            )
        )
    return out
