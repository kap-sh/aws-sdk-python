"""Generated from Smithy shape ``com.amazonaws.chime#BusinessCallingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.string


class BusinessCallingSettings(TypedDict):
    cdr_bucket: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The Amazon S3 bucket designated for call detail record storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BusinessCallingSettings) -> dict:
    out: dict = {}
    if "cdr_bucket" in value:
        out["CdrBucket"] = value["cdr_bucket"]
    return out


def deserialize_json(data: dict) -> BusinessCallingSettings:
    out: BusinessCallingSettings = {}  # type: ignore[typeddict-item]
    if "CdrBucket" in data:
        out["cdr_bucket"] = data["CdrBucket"]
    return out
