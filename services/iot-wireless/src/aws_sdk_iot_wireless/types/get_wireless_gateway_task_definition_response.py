"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetWirelessGatewayTaskDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.auto_create_tasks
    import aws_sdk_iot_wireless.types.update_wireless_gateway_task_create
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn
    import aws_sdk_iot_wireless.types.wireless_gateway_task_name


class GetWirelessGatewayTaskDefinitionResponse(TypedDict, closed=True):
    auto_create_tasks: "aws_sdk_iot_wireless.types.auto_create_tasks.AutoCreateTasks"
    """<p>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If <code>false</code>, the task must me created by calling <code>CreateWirelessGatewayTask</code>.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_name.WirelessGatewayTaskName"
    ]
    """<p>The name of the resource.</p>"""
    update: NotRequired[
        "aws_sdk_iot_wireless.types.update_wireless_gateway_task_create.UpdateWirelessGatewayTaskCreate"
    ]
    """<p>Information about the gateways to update.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn.WirelessGatewayTaskDefinitionArn"
    ]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWirelessGatewayTaskDefinitionResponse) -> dict:
    out: dict = {}
    out["AutoCreateTasks"] = value.get("auto_create_tasks", False)
    if "name" in value:
        out["Name"] = value["name"]
    if "update" in value:
        import aws_sdk_iot_wireless.types.update_wireless_gateway_task_create

        out["Update"] = (
            aws_sdk_iot_wireless.types.update_wireless_gateway_task_create.serialize_json(
                value["update"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetWirelessGatewayTaskDefinitionResponse:
    out: GetWirelessGatewayTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "AutoCreateTasks" in data:
        out["auto_create_tasks"] = data["AutoCreateTasks"]
    else:
        out["auto_create_tasks"] = False
    if "Name" in data:
        out["name"] = data["Name"]
    if "Update" in data:
        import aws_sdk_iot_wireless.types.update_wireless_gateway_task_create

        out["update"] = (
            aws_sdk_iot_wireless.types.update_wireless_gateway_task_create.deserialize_json(
                data["Update"]
            )
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
