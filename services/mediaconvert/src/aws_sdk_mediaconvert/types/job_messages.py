"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobMessages``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__string


class JobMessages(TypedDict):
    info: NotRequired["aws_sdk_mediaconvert.types.__list_of__string.__listOf__string"]
    """List of messages that are informational only and don't indicate a problem with your job."""
    warning: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__string.__listOf__string"
    ]
    """List of messages that warn about conditions that might cause your job not to run or to fail."""


# --- restJson1 ser/de ---
def serialize_json(value: JobMessages) -> dict:
    out: dict = {}
    if "info" in value:
        import aws_sdk_mediaconvert.types.__list_of__string

        out["info"] = aws_sdk_mediaconvert.types.__list_of__string.serialize_json(
            value["info"]
        )
    if "warning" in value:
        import aws_sdk_mediaconvert.types.__list_of__string

        out["warning"] = aws_sdk_mediaconvert.types.__list_of__string.serialize_json(
            value["warning"]
        )
    return out


def deserialize_json(data: dict) -> JobMessages:
    out: JobMessages = {}  # type: ignore[typeddict-item]
    if "info" in data:
        import aws_sdk_mediaconvert.types.__list_of__string

        out["info"] = aws_sdk_mediaconvert.types.__list_of__string.deserialize_json(
            data["info"]
        )
    if "warning" in data:
        import aws_sdk_mediaconvert.types.__list_of__string

        out["warning"] = aws_sdk_mediaconvert.types.__list_of__string.deserialize_json(
            data["warning"]
        )
    return out
