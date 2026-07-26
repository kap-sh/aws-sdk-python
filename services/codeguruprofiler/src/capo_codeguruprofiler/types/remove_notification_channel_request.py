"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#RemoveNotificationChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.channel_id
    import capo_codeguruprofiler.types.profiling_group_name


class RemoveNotificationChannelRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group we want to change notification configuration for.</p>"""
    channel_id: "capo_codeguruprofiler.types.channel_id.ChannelId"
    """<p>The id of the channel that we want to stop receiving notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveNotificationChannelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveNotificationChannelRequest:
    out: RemoveNotificationChannelRequest = {}  # type: ignore[typeddict-item]
    return out
