"""Generated from Smithy shape ``com.amazonaws.iot#StreamSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.stream_arn
    import aws_sdk_iot.types.stream_description
    import aws_sdk_iot.types.stream_id
    import aws_sdk_iot.types.stream_version


class StreamSummary(TypedDict, closed=True):
    stream_id: NotRequired["aws_sdk_iot.types.stream_id.StreamId"]
    """<p>The stream ID.</p>"""
    stream_arn: NotRequired["aws_sdk_iot.types.stream_arn.StreamArn"]
    """<p>The stream ARN.</p>"""
    stream_version: NotRequired["aws_sdk_iot.types.stream_version.StreamVersion"]
    """<p>The stream version.</p>"""
    description: NotRequired["aws_sdk_iot.types.stream_description.StreamDescription"]
    """<p>A description of the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamSummary) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "stream_arn" in value:
        out["streamArn"] = value["stream_arn"]
    if "stream_version" in value:
        out["streamVersion"] = value["stream_version"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StreamSummary:
    out: StreamSummary = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "streamArn" in data:
        out["stream_arn"] = data["streamArn"]
    if "streamVersion" in data:
        out["stream_version"] = data["streamVersion"]
    if "description" in data:
        out["description"] = data["description"]
    return out
