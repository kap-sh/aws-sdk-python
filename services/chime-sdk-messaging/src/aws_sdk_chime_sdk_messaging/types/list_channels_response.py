"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_summary_list
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelsResponse(TypedDict):
    channels: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_summary_list.ChannelSummaryList"
    ]
    """<p>The information about each channel.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of channels is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_summary_list

        out["Channels"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary_list.serialize_json(
                value["channels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelsResponse:
    out: ListChannelsResponse = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_summary_list

        out["channels"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary_list.deserialize_json(
                data["Channels"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
