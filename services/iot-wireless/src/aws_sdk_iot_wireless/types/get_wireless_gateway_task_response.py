"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.iso_date_time_string
    import aws_sdk_iot_wireless.types.wireless_gateway_id
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id
    import aws_sdk_iot_wireless.types.wireless_gateway_task_status


class GetWirelessGatewayTaskResponse(TypedDict, closed=True):
    wireless_gateway_id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    ]
    """<p>The ID of the wireless gateway.</p>"""
    wireless_gateway_task_definition_id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    ]
    """<p>The ID of the WirelessGatewayTask.</p>"""
    last_uplink_received_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the most recent uplink was received.</p> <note> <p>This value is only valid for 3 months.</p> </note>"""
    task_created_at: NotRequired[
        "aws_sdk_iot_wireless.types.iso_date_time_string.ISODateTimeString"
    ]
    """<p>The date and time when the task was created.</p>"""
    status: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_status.WirelessGatewayTaskStatus"
    ]
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayTaskResponse) -> dict:
    out: dict = {}
    if "wireless_gateway_id" in value:
        out["WirelessGatewayId"] = value["wireless_gateway_id"]
    if "wireless_gateway_task_definition_id" in value:
        out["WirelessGatewayTaskDefinitionId"] = value[
            "wireless_gateway_task_definition_id"
        ]
    if "last_uplink_received_at" in value:
        out["LastUplinkReceivedAt"] = value["last_uplink_received_at"]
    if "task_created_at" in value:
        out["TaskCreatedAt"] = value["task_created_at"]
    if "status" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_status

        out["Status"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayTaskResponse:
    out: GetWirelessGatewayTaskResponse = {}  # type: ignore[typeddict-item]
    if "WirelessGatewayId" in data:
        out["wireless_gateway_id"] = data["WirelessGatewayId"]
    if "WirelessGatewayTaskDefinitionId" in data:
        out["wireless_gateway_task_definition_id"] = data[
            "WirelessGatewayTaskDefinitionId"
        ]
    if "LastUplinkReceivedAt" in data:
        out["last_uplink_received_at"] = data["LastUplinkReceivedAt"]
    if "TaskCreatedAt" in data:
        out["task_created_at"] = data["TaskCreatedAt"]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_status

        out["status"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_status.deserialize_json(
                data["Status"]
            )
        )
    return out
