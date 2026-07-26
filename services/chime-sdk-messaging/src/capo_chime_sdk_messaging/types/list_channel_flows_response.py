"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelFlowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_flow_summary_list
    import capo_chime_sdk_messaging.types.next_token


class ListChannelFlowsResponse(TypedDict, closed=True):
    channel_flows: NotRequired[
        "capo_chime_sdk_messaging.types.channel_flow_summary_list.ChannelFlowSummaryList"
    ]
    """<p>The information about each channel flow.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelFlowsResponse) -> dict:
    out: dict = {}
    if "channel_flows" in value:
        import capo_chime_sdk_messaging.types.channel_flow_summary_list

        out["ChannelFlows"] = (
            capo_chime_sdk_messaging.types.channel_flow_summary_list.serialize_json(
                value["channel_flows"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelFlowsResponse:
    out: ListChannelFlowsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelFlows" in data:
        import capo_chime_sdk_messaging.types.channel_flow_summary_list

        out["channel_flows"] = (
            capo_chime_sdk_messaging.types.channel_flow_summary_list.deserialize_json(
                data["ChannelFlows"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
