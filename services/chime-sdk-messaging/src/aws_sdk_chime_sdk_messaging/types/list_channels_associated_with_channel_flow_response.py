"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsAssociatedWithChannelFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelsAssociatedWithChannelFlowResponse(TypedDict, closed=True):
    channels: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.ChannelAssociatedWithFlowSummaryList"
    ]
    """<p>The information about each channel.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channels are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsAssociatedWithChannelFlowResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list

        out["Channels"] = (
            aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.serialize_json(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsAssociatedWithChannelFlowResponse:
    out: ListChannelsAssociatedWithChannelFlowResponse = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list

        out["channels"] = (
            aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary_list.deserialize_json(
                data["Channels"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
