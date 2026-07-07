"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class GetWirelessGatewayStatisticsRequest(TypedDict, closed=True):
    wireless_gateway_id: (
        "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    )
    """<p>The ID of the wireless gateway for which to get the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayStatisticsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayStatisticsRequest:
    out: GetWirelessGatewayStatisticsRequest = {}  # type: ignore[typeddict-item]
    return out
