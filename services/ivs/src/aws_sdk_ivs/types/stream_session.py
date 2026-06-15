"""Generated from Smithy shape ``com.amazonaws.ivs#StreamSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel
    import aws_sdk_ivs.types.ingest_configuration
    import aws_sdk_ivs.types.ingest_configurations
    import aws_sdk_ivs.types.recording_configuration
    import aws_sdk_ivs.types.stream_events
    import aws_sdk_ivs.types.stream_id
    import aws_sdk_ivs.types.time


class StreamSession(TypedDict):
    stream_id: NotRequired["aws_sdk_ivs.types.stream_id.StreamId"]
    """<p>Unique identifier for a live or previously live stream in the specified channel.</p>"""
    start_time: NotRequired["aws_sdk_ivs.types.time.Time"]
    """<p>Time when the channel went live. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    end_time: NotRequired["aws_sdk_ivs.types.time.Time"]
    """<p>Time when the channel went offline. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>. For live streams, this is <code>NULL</code>.</p>"""
    channel: NotRequired["aws_sdk_ivs.types.channel.Channel"]
    """<p>The properties of the channel at the time of going live.</p>"""
    ingest_configuration: NotRequired[
        "aws_sdk_ivs.types.ingest_configuration.IngestConfiguration"
    ]
    """<p>The properties of the incoming RTMP stream.</p> <p> <b>Note:</b> <code>ingestConfiguration</code> is deprecated in favor of <code>ingestConfigurations</code> but retained to ensure backward compatibility. If multitrack is not enabled, <code>ingestConfiguration</code> and <code>ingestConfigurations</code> contain the same data, namely information about Track0 (the sole track). If multitrack is enabled, <code>ingestConfiguration</code> contains data for only the first track (Track0) and <code>ingestConfigurations</code> contains data for all tracks.</p>"""
    ingest_configurations: NotRequired[
        "aws_sdk_ivs.types.ingest_configurations.IngestConfigurations"
    ]
    """<p>The properties of the incoming RTMP stream. If multitrack is enabled, <code>ingestConfigurations</code> contains data for all tracks; otherwise, it contains data only for Track0 (the sole track).</p>"""
    recording_configuration: NotRequired[
        "aws_sdk_ivs.types.recording_configuration.RecordingConfiguration"
    ]
    """<p>The properties of recording the live stream.</p>"""
    truncated_events: NotRequired["aws_sdk_ivs.types.stream_events.StreamEvents"]
    r"""<p>List of Amazon IVS events that the stream encountered. The list is sorted by most recent events and contains up to 500 events. For Amazon IVS events, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\">Using Amazon EventBridge with Amazon IVS</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSession) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "start_time" in value:
        import aws_sdk_ivs.types.time

        out["startTime"] = aws_sdk_ivs.types.time.serialize_json(value["start_time"])
    if "end_time" in value:
        import aws_sdk_ivs.types.time

        out["endTime"] = aws_sdk_ivs.types.time.serialize_json(value["end_time"])
    if "channel" in value:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.serialize_json(value["channel"])
    if "ingest_configuration" in value:
        import aws_sdk_ivs.types.ingest_configuration

        out["ingestConfiguration"] = (
            aws_sdk_ivs.types.ingest_configuration.serialize_json(
                value["ingest_configuration"]
            )
        )
    if "ingest_configurations" in value:
        import aws_sdk_ivs.types.ingest_configurations

        out["ingestConfigurations"] = (
            aws_sdk_ivs.types.ingest_configurations.serialize_json(
                value["ingest_configurations"]
            )
        )
    if "recording_configuration" in value:
        import aws_sdk_ivs.types.recording_configuration

        out["recordingConfiguration"] = (
            aws_sdk_ivs.types.recording_configuration.serialize_json(
                value["recording_configuration"]
            )
        )
    if "truncated_events" in value:
        import aws_sdk_ivs.types.stream_events

        out["truncatedEvents"] = aws_sdk_ivs.types.stream_events.serialize_json(
            value["truncated_events"]
        )
    return out


def deserialize_json(data: dict) -> StreamSession:
    out: StreamSession = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "startTime" in data:
        import aws_sdk_ivs.types.time

        out["start_time"] = aws_sdk_ivs.types.time.deserialize_json(data["startTime"])
    if "endTime" in data:
        import aws_sdk_ivs.types.time

        out["end_time"] = aws_sdk_ivs.types.time.deserialize_json(data["endTime"])
    if "channel" in data:
        import aws_sdk_ivs.types.channel

        out["channel"] = aws_sdk_ivs.types.channel.deserialize_json(data["channel"])
    if "ingestConfiguration" in data:
        import aws_sdk_ivs.types.ingest_configuration

        out["ingest_configuration"] = (
            aws_sdk_ivs.types.ingest_configuration.deserialize_json(
                data["ingestConfiguration"]
            )
        )
    if "ingestConfigurations" in data:
        import aws_sdk_ivs.types.ingest_configurations

        out["ingest_configurations"] = (
            aws_sdk_ivs.types.ingest_configurations.deserialize_json(
                data["ingestConfigurations"]
            )
        )
    if "recordingConfiguration" in data:
        import aws_sdk_ivs.types.recording_configuration

        out["recording_configuration"] = (
            aws_sdk_ivs.types.recording_configuration.deserialize_json(
                data["recordingConfiguration"]
            )
        )
    if "truncatedEvents" in data:
        import aws_sdk_ivs.types.stream_events

        out["truncated_events"] = aws_sdk_ivs.types.stream_events.deserialize_json(
            data["truncatedEvents"]
        )
    return out
