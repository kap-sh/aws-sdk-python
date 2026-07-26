"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListSignalingChannelsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_name_condition
    import capo_kinesis_video.types.list_streams_input_limit
    import capo_kinesis_video.types.next_token


class ListSignalingChannelsInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_kinesis_video.types.list_streams_input_limit.ListStreamsInputLimit"
    ]
    """<p>The maximum number of channels to return in the response. The default is 500.</p>"""
    next_token: NotRequired["capo_kinesis_video.types.next_token.NextToken"]
    """<p>If you specify this parameter, when the result of a <code>ListSignalingChannels</code> operation is truncated, the call returns the <code>NextToken</code> in the response. To get another batch of channels, provide this token in your next request.</p>"""
    channel_name_condition: NotRequired[
        "capo_kinesis_video.types.channel_name_condition.ChannelNameCondition"
    ]
    """<p>Optional: Returns only the channels that satisfy a specific condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSignalingChannelsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "channel_name_condition" in value:
        import capo_kinesis_video.types.channel_name_condition

        out["ChannelNameCondition"] = (
            capo_kinesis_video.types.channel_name_condition.serialize_json(
                value["channel_name_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSignalingChannelsInput:
    out: ListSignalingChannelsInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ChannelNameCondition" in data:
        import capo_kinesis_video.types.channel_name_condition

        out["channel_name_condition"] = (
            capo_kinesis_video.types.channel_name_condition.deserialize_json(
                data["ChannelNameCondition"]
            )
        )
    return out
