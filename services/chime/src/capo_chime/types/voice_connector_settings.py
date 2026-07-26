"""Generated from Smithy shape ``com.amazonaws.chime#VoiceConnectorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.string


class VoiceConnectorSettings(TypedDict, closed=True):
    cdr_bucket: NotRequired["capo_chime.types.string.String"]
    """<p>The Amazon S3 bucket designated for call detail record storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorSettings) -> dict:
    out: dict = {}
    if "cdr_bucket" in value:
        out["CdrBucket"] = value["cdr_bucket"]
    return out


def deserialize_json(data: dict) -> VoiceConnectorSettings:
    out: VoiceConnectorSettings = {}  # type: ignore[typeddict-item]
    if "CdrBucket" in data:
        out["cdr_bucket"] = data["CdrBucket"]
    return out
