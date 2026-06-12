"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Metadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__long
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__timestamp_unix


class Metadata(TypedDict):
    e_tag: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The entity tag (ETag) of the file."""
    file_size: NotRequired["aws_sdk_mediaconvert.types.__long.__long"]
    """The size of the media file, in bytes."""
    last_modified: NotRequired[
        "aws_sdk_mediaconvert.types.__timestamp_unix.__timestampUnix"
    ]
    """The last modification timestamp of the media file, in Unix time."""
    mime_type: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """The MIME type of the media file."""


# --- restJson1 ser/de ---
def serialize_json(value: Metadata) -> dict:
    out: dict = {}
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    if "last_modified" in value:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["lastModified"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.serialize_json(
                value["last_modified"]
            )
        )
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}  # type: ignore[typeddict-item]
    if "eTag" in data:
        out["e_tag"] = data["eTag"]
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    if "lastModified" in data:
        import aws_sdk_mediaconvert.types.__timestamp_unix

        out["last_modified"] = (
            aws_sdk_mediaconvert.types.__timestamp_unix.deserialize_json(
                data["lastModified"]
            )
        )
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    return out
