"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MultiViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern_s3_https


class MultiViewInput(TypedDict, closed=True):
    file_input: NotRequired[
        "capo_mediaconvert.types.__string_pattern_s3_https.__stringPatternS3Https"
    ]
    """Specify the input file S3, HTTP, or HTTPS URL for your right eye view video."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiViewInput) -> dict:
    out: dict = {}
    if "file_input" in value:
        out["fileInput"] = value["file_input"]
    return out


def deserialize_json(data: dict) -> MultiViewInput:
    out: MultiViewInput = {}  # type: ignore[typeddict-item]
    if "fileInput" in data:
        out["file_input"] = data["fileInput"]
    return out
