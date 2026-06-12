"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#RemoveNotificationChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.channel_id
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class RemoveNotificationChannelRequest(TypedDict):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group we want to change notification configuration for.</p>"""
    channel_id: "aws_sdk_codeguruprofiler.types.channel_id.ChannelId"
    """<p>The id of the channel that we want to stop receiving notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelRequest:
    out: RemoveNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out
