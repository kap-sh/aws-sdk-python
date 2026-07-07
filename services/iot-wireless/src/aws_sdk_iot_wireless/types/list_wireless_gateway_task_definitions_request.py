"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListWirelessGatewayTaskDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.wireless_gateway_task_definition_type


class ListWirelessGatewayTaskDefinitionsRequest(TypedDict, closed=True):
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    """<p>The maximum number of results to return in this operation.</p>"""
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    task_definition_type: NotRequired[
        "aws_sdk_iot_wireless.types.wireless_gateway_task_definition_type.WirelessGatewayTaskDefinitionType"
    ]
    """<p>A filter to list only the wireless gateway task definitions that use this task definition type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWirelessGatewayTaskDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWirelessGatewayTaskDefinitionsRequest:
    out: ListWirelessGatewayTaskDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
