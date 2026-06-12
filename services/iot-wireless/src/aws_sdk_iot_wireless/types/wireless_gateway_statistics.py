"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.description
    import aws_sdk_iot_wireless.types.iso_date_time_string
    import aws_sdk_iot_wireless.types.lo_ra_wan_gateway
    import aws_sdk_iot_wireless.types.wireless_gateway_arn
    import aws_sdk_iot_wireless.types.wireless_gateway_id
    import aws_sdk_iot_wireless.types.wireless_gateway_name


class WirelessGatewayStatistics(TypedDict):
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_arn.WirelessGatewayArn"
    ]
    """<p>The Amazon Resource Name of the resource.</p>"""
    id: NotRequired["aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"]
    """<p>The ID of the wireless gateway reporting the data.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
    ]
    """<p>The name of the resource.</p>"""
    description: NotRequired["aws_sdk_iot_wireless.types.description.Description"]
    """<p>The description of the resource.</p>"""
    lo_ra_wan: NotRequired[
        "aws_sdk_iot_wireless.types.lo_ra_wan_gateway.LoRaWANGateway"
    ]
    """<p>LoRaWAN gateway info.</p>"""
    last_uplink_received_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>This value is only valid for 3 months.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayStatistics) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "lo_ra_wan" in value:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway

        out["LoRaWAN"] = aws_sdk_iot_wireless.types.lo_ra_wan_gateway.serialize_json(
            value["lo_ra_wan"]
        )
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    return out


def deserialize_json(data: dict) -> WirelessGatewayStatistics:
    out: WirelessGatewayStatistics = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LoRaWAN" in data:
        import aws_sdk_iot_wireless.types.lo_ra_wan_gateway

        out["lo_ra_wan"] = (
            aws_sdk_iot_wireless.types.lo_ra_wan_gateway.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "LastUplinkReceivedAt" in data:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    return out
