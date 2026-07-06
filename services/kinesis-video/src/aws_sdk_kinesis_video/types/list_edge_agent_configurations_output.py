"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list
    import aws_sdk_kinesis_video.types.next_token


class ListEdgeAgentConfigurationsOutput(TypedDict, closed=True):
    edge_configs: NotRequired[
        "aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list.ListEdgeAgentConfigurationsEdgeConfigList"
    ]
    """<p>A description of a single stream's edge configuration.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_video.types.next_token.NextToken"]
    """<p>If the response is truncated, the call returns this element with a given token. To get the next batch of edge configurations, use this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsOutput) -> dict:
    out: dict = {}
    if "edge_configs" in value:
        import aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list

        out["EdgeConfigs"] = (
            aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list.serialize_json(
                value["edge_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEdgeAgentConfigurationsOutput:
    out: ListEdgeAgentConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "EdgeConfigs" in data:
        import aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list

        out["edge_configs"] = (
            aws_sdk_kinesis_video.types.list_edge_agent_configurations_edge_config_list.deserialize_json(
                data["EdgeConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
