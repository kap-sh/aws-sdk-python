"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.connection_status
    import aws_sdk_iot_wireless.types.iso_date_time_string
    import aws_sdk_iot_wireless.types.wireless_gateway_id


class GetWirelessGatewayStatisticsResponse(TypedDict, closed=True):
    wireless_gateway_id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    ]
    """<p>The ID of the wireless gateway.</p>"""
    last_uplink_received_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>This value is only valid for 3 months.</p> </note>"""
    connection_status: NotRequired[
        "aws_sdk_iot_wireless.types.connection_status.ConnectionStatus"
    ]
    """<p>The connection status of the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayStatisticsResponse) -> dict:
    out: dict = {}
    if "wireless_gateway_id" in value:
        out["WirelessGatewayId"] = value["wireless_gateway_id"]
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    if "connection_status" in value:
        import aws_sdk_iot_wireless.types.connection_status

        out["ConnectionStatus"] = (
            aws_sdk_iot_wireless.types.connection_status.serialize_json(
                value["connection_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayStatisticsResponse:
    out: GetWirelessGatewayStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "WirelessGatewayId" in data:
        out["wireless_gateway_id"] = data["WirelessGatewayId"]
    if "LastUplinkReceivedAt" in data:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    if "ConnectionStatus" in data:
        import aws_sdk_iot_wireless.types.connection_status

        out["connection_status"] = (
            aws_sdk_iot_wireless.types.connection_status.deserialize_json(
                data["ConnectionStatus"]
            )
        )
    return out
