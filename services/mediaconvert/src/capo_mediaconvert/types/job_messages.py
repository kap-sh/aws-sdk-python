"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobMessages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of__string


class JobMessages(TypedDict, closed=True):
    info: NotRequired["capo_mediaconvert.types.__list_of__string.__listOf__string"]
    """List of messages that are informational only and don't indicate a problem with your job."""
    warning: NotRequired["capo_mediaconvert.types.__list_of__string.__listOf__string"]
    """List of messages that warn about conditions that might cause your job not to run or to fail."""


# --- restJson1 ser/de ---
def serialize_json(value: JobMessages) -> dict:
    out: dict = {}
    if "info" in value:
        import capo_mediaconvert.types.__list_of__string

        out["info"] = capo_mediaconvert.types.__list_of__string.serialize_json(
            value["info"]
        )
    if "warning" in value:
        import capo_mediaconvert.types.__list_of__string

        out["warning"] = capo_mediaconvert.types.__list_of__string.serialize_json(
            value["warning"]
        )
    return out


def deserialize_json(data: dict) -> JobMessages:
    out: JobMessages = {}  # type: ignore[typeddict-item]
    if "info" in data:
        import capo_mediaconvert.types.__list_of__string

        out["info"] = capo_mediaconvert.types.__list_of__string.deserialize_json(
            data["info"]
        )
    if "warning" in data:
        import capo_mediaconvert.types.__list_of__string

        out["warning"] = capo_mediaconvert.types.__list_of__string.deserialize_json(
            data["warning"]
        )
    return out
