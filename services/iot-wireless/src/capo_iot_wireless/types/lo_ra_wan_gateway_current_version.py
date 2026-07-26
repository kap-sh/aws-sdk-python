"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGatewayCurrentVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.lo_ra_wan_gateway_version


class LoRaWANGatewayCurrentVersion(TypedDict, closed=True):
    current_version: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_gateway_version.LoRaWANGatewayVersion"
    ]
    """<p>The version of the gateways that should receive the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGatewayCurrentVersion) -> dict:
    out: dict = {}
    if "current_version" in value:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["CurrentVersion"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.serialize_json(
                value["current_version"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANGatewayCurrentVersion:
    out: LoRaWANGatewayCurrentVersion = {}  # type: ignore[typeddict-item]
    if "CurrentVersion" in data:
        import capo_iot_wireless.types.lo_ra_wan_gateway_version

        out["current_version"] = (
            capo_iot_wireless.types.lo_ra_wan_gateway_version.deserialize_json(
                data["CurrentVersion"]
            )
        )
    return out
