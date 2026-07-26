"""Generated from Smithy shape ``com.amazonaws.ivs#StreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.channel_arn
    import capo_ivs.types.stream_health
    import capo_ivs.types.stream_id
    import capo_ivs.types.stream_start_time
    import capo_ivs.types.stream_state
    import capo_ivs.types.stream_viewer_count


class StreamSummary(TypedDict, closed=True):
    channel_arn: NotRequired["capo_ivs.types.channel_arn.ChannelArn"]
    """<p>Channel ARN for the stream.</p>"""
    stream_id: NotRequired["capo_ivs.types.stream_id.StreamId"]
    """<p>Unique identifier for a live or previously live stream in the specified channel.</p>"""
    state: NotRequired["capo_ivs.types.stream_state.StreamState"]
    r"""<p>The stream’s state. Do not rely on the <code>OFFLINE</code> state, as the API may not return it; instead, a \"NotBroadcasting\" error will indicate that the stream is not live.</p>"""
    health: NotRequired["capo_ivs.types.stream_health.StreamHealth"]
    """<p>The stream’s health.</p>"""
    viewer_count: "capo_ivs.types.stream_viewer_count.StreamViewerCount"
    """<p>A count of concurrent views of the stream. Typically, a new view appears in <code>viewerCount</code> within 15 seconds of when video playback starts and a view is removed from <code>viewerCount</code> within 1 minute of when video playback ends. A value of -1 indicates that the request timed out; in this case, retry.</p>"""
    start_time: NotRequired["capo_ivs.types.stream_start_time.StreamStartTime"]
    """<p>Time of the stream’s start. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSummary) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "state" in value:
        out["state"] = value["state"]
    if "health" in value:
        out["health"] = value["health"]
    out["viewerCount"] = value.get("viewer_count", 0)
    if "start_time" in value:
        import capo_ivs.types.stream_start_time

        out["startTime"] = capo_ivs.types.stream_start_time.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> StreamSummary:
    out: StreamSummary = {}  # type: ignore[typeddict-item]
    if "channelArn" in data:
        out["channel_arn"] = data["channelArn"]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "state" in data:
        out["state"] = data["state"]
    if "health" in data:
        out["health"] = data["health"]
    if "viewerCount" in data:
        out["viewer_count"] = data["viewerCount"]
    else:
        out["viewer_count"] = 0
    if "startTime" in data:
        import capo_ivs.types.stream_start_time

        out["start_time"] = capo_ivs.types.stream_start_time.deserialize_json(
            data["startTime"]
        )
    return out
