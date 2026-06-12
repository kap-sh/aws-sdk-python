"""Generated from Smithy shape ``com.amazonaws.iot#Stream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.file_id
    import aws_sdk_iot.types.stream_id


class Stream(TypedDict):
    stream_id: NotRequired["aws_sdk_iot.types.stream_id.StreamId"]
    """<p>The stream ID.</p>"""
    file_id: NotRequired["aws_sdk_iot.types.file_id.FileId"]
    """<p>The ID of a file associated with a stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stream) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    return out


def deserialize_json(data: dict) -> Stream:
    out: Stream = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    return out
