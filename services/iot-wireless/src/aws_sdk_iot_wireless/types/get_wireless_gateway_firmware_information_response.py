"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayFirmwareInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version


class GetWirelessGatewayFirmwareInformationResponse(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version.LoRaWANGatewayCurrentVersion"
    ]
    """<p>Information about the wireless gateway's firmware.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayFirmwareInformationResponse) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version

        out["LoRaWAN"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version.serialize_json(
                value["lo_ra_wan"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayFirmwareInformationResponse:
    out: GetWirelessGatewayFirmwareInformationResponse = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway_current_version.deserialize_json(
                data["LoRaWAN"]
            )
        )
    return out
