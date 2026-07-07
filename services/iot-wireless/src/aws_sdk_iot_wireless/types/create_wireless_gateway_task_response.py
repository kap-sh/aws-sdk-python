"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id
    import aws_sdk_iot_wireless.types.wireless_gateway_task_status


class CreateWirelessGatewayTaskResponse(TypedDict, closed=True):
    wireless_gateway_task_definition_id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    ]
    """<p>The ID of the WirelessGatewayTaskDefinition.</p>"""
    status: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_status.WirelessGatewayTaskStatus"
    ]
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayTaskResponse) -> dict:
    out: dict = {}
    if "wireless_gateway_task_definition_id" in value:
        out["WirelessGatewayTaskDefinitionId"] = value[
            "wireless_gateway_task_definition_id"
        ]
    if "status" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_status

        out["Status"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayTaskResponse:
    out: CreateWirelessGatewayTaskResponse = {}  # type: ignore[typeddict-item]
    if "WirelessGatewayTaskDefinitionId" in data:
        out["wireless_gateway_task_definition_id"] = data[
            "WirelessGatewayTaskDefinitionId"
        ]
    if "Status" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_status

        out["status"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_status.deserialize_json(
                data["Status"]
            )
        )
    return out
