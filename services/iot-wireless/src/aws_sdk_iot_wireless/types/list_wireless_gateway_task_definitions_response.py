"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessGatewayTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list


class ListWirelessGatewayTaskDefinitionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    task_definitions: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list.WirelessGatewayTaskDefinitionList"
    ]
    """<p>The list of task definitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessGatewayTaskDefinitionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "task_definitions" in value:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list

        out["TaskDefinitions"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list.serialize_json(
                value["task_definitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListWirelessGatewayTaskDefinitionsResponse:
    out: ListWirelessGatewayTaskDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TaskDefinitions" in data:
        import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list

        out["task_definitions"] = (
            aws_sdk_iot_wireless.types.wireless_gateway_task_definition_list.deserialize_json(
                data["TaskDefinitions"]
            )
        )
    return out
