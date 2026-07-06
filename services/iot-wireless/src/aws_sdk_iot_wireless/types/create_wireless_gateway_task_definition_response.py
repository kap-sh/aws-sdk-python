"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateWirelessGatewayTaskDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id


class CreateWirelessGatewayTaskDefinitionResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId"
    ]
    """<p>The ID of the new wireless gateway task definition.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_arn.WirelessGatewayTaskDefinitionArn"
    ]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWirelessGatewayTaskDefinitionResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateWirelessGatewayTaskDefinitionResponse:
    out: CreateWirelessGatewayTaskDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
