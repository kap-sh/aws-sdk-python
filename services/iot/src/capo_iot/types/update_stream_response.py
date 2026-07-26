"""Generated from Smithy shape ``com.amazonaws.iot#UpdateStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.stream_arn
    import capo_iot.types.stream_description
    import capo_iot.types.stream_id
    import capo_iot.types.stream_version


class UpdateStreamResponse(TypedDict, closed=True):
    stream_id: NotRequired["capo_iot.types.stream_id.StreamId"]
    """<p>The stream ID.</p>"""
    stream_arn: NotRequired["capo_iot.types.stream_arn.StreamArn"]
    """<p>The stream ARN.</p>"""
    description: NotRequired["capo_iot.types.stream_description.StreamDescription"]
    """<p>A description of the stream.</p>"""
    stream_version: NotRequired["capo_iot.types.stream_version.StreamVersion"]
    """<p>The stream version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStreamResponse) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "stream_arn" in value:
        out["streamArn"] = value["stream_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "stream_version" in value:
        out["streamVersion"] = value["stream_version"]
    return out


def deserialize_json(data: dict) -> UpdateStreamResponse:
    out: UpdateStreamResponse = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "streamArn" in data:
        out["stream_arn"] = data["streamArn"]
    if "description" in data:
        out["description"] = data["description"]
    if "streamVersion" in data:
        out["stream_version"] = data["streamVersion"]
    return out
