"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ProbeInputFile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class ProbeInputFile(TypedDict):
    file_url: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Specify the S3, HTTP, or HTTPS URL for your media file."""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeInputFile) -> dict:
    out: dict = {}
    if "file_url" in value:
        out["fileUrl"] = value["file_url"]
    return out


def deserialize_json(data: dict) -> ProbeInputFile:
    out: ProbeInputFile = {}  # type: ignore[typeddict-item]
    if "fileUrl" in data:
        out["file_url"] = data["fileUrl"]
    return out
