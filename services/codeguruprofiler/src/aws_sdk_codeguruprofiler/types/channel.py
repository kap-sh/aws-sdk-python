"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.channel_id
    import aws_sdk_codeguruprofiler.types.channel_uri
    import aws_sdk_codeguruprofiler.types.event_publishers


class Channel(TypedDict, closed=True):
    id: NotRequired["aws_sdk_codeguruprofiler.types.channel_id.ChannelId"]
    """<p>Unique identifier for each <code>Channel</code> in the notification configuration of a Profiling Group. A random UUID for channelId is used when adding a channel to the notification configuration if not specified in the request.</p>"""
    uri: "aws_sdk_codeguruprofiler.types.channel_uri.ChannelUri"
    """<p>Unique arn of the resource to be used for notifications. We support a valid SNS topic arn as a channel uri.</p>"""
    event_publishers: "aws_sdk_codeguruprofiler.types.event_publishers.EventPublishers"
    """<p>List of publishers for different type of events that may be detected in an application from the profile. Anomaly detection is the only event publisher in Profiler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Channel) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["uri"] = value["uri"]
    import aws_sdk_codeguruprofiler.types.event_publishers

    out["eventPublishers"] = (
        aws_sdk_codeguruprofiler.types.event_publishers.serialize_json(
            value["event_publishers"]
        )
    )
    return out


def deserialize_json(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("Channel.uri required")
    if "eventPublishers" in data:
        import aws_sdk_codeguruprofiler.types.event_publishers

        out["event_publishers"] = (
            aws_sdk_codeguruprofiler.types.event_publishers.deserialize_json(
                data["eventPublishers"]
            )
        )
    else:
        raise DeserializationError("Channel.event_publishers required")
    return out
