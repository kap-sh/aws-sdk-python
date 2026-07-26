"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANUpdateGatewayTaskEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lo_ra_wan_gateway_version


class LoRaWANUpdateGatewayTaskEntry(TypedDict, closed=True):
    current_version: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The version of the gateways that should receive the update.</p>"""
    update_version: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The firmware version to update the gateway to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANUpdateGatewayTaskEntry) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> LoRaWANUpdateGatewayTaskEntry:
    out: LoRaWANUpdateGatewayTaskEntry = {}  # type: ignore[typeddict-item]
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
