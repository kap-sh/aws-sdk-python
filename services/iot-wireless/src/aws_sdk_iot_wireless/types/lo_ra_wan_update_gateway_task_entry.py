"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANUpdateGatewayTaskEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version


class LoRaWANUpdateGatewayTaskEntry(TypedDict):
    current_version: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The version of the gateways that should receive the update.</p>"""
    update_version: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The firmware version to update the gateway to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANUpdateGatewayTaskEntry) -> dict:
    out: dict = {}
    if "current_version" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version

        out["CurrentVersion"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.serialize_json(
                value["current_version"]
            )
        )
    if "update_version" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version

        out["UpdateVersion"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.serialize_json(
                value["update_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANUpdateGatewayTaskEntry:
    out: LoRaWANUpdateGatewayTaskEntry = {}  # type: ignore[typeddict-item]
    if "CurrentVersion" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version

        out["current_version"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.deserialize_json(
                data["CurrentVersion"]
            )
        )
    if "UpdateVersion" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version

        out["update_version"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_version.deserialize_json(
                data["UpdateVersion"]
            )
        )
    return out
