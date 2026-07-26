"""Generated from Smithy shape ``com.amazonaws.iot#StreamFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.file_id
    import capo_iot.types.s3_location


class StreamFile(TypedDict, closed=True):
    file_id: NotRequired["capo_iot.types.file_id.FileId"]
    """<p>The file ID.</p>"""
    s3_location: NotRequired["capo_iot.types.s3_location.S3Location"]
    """<p>The location of the file in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamFile) -> dict:
    out: dict = {}
    if "file_id" in value:
        out["fileId"] = value["file_id"]
    if "s3_location" in value:
        import capo_iot.types.s3_location

        out["s3Location"] = capo_iot.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> StreamFile:
    out: StreamFile = {}  # type: ignore[typeddict-item]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    if "s3Location" in data:
        import capo_iot.types.s3_location

        out["s3_location"] = capo_iot.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out
