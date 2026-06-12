"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.hub_device_arn
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_input_limit
    import aws_sdk_kinesis_video.types.next_token


class ListEdgeAgentConfigurationsInput(TypedDict):
    hub_device_arn: "aws_sdk_kinesis_video.types.hub_device_arn.HubDeviceArn"
    """<p>The \"Internet of Things (IoT) Thing\" Arn of the edge agent.</p>"""
    max_results: NotRequired[
        "aws_sdk_kinesis_video.types.list_edge_agent_configurations_input_limit.ListEdgeAgentConfigurationsInputLimit"
    ]
    """<p>The maximum number of edge configurations to return in the response. The default is 5.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter, when the result of a <code>ListEdgeAgentConfigurations</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of edge configurations, provide this token in your next request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsInput) -> dict:
    out: dict = {}
    out["HubDeviceArn"] = value["hub_device_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEdgeAgentConfigurationsInput:
    out: ListEdgeAgentConfigurationsInput = {}  # type: ignore[typeddict-item]
    if "HubDeviceArn" in data:
        out["hub_device_arn"] = data["HubDeviceArn"]
    else:
        raise DeserializationError(
            "ListEdgeAgentConfigurationsInput.hub_device_arn required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
