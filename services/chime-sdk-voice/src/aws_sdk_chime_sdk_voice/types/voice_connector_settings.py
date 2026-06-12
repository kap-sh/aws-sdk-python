"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.string


class VoiceConnectorSettings(TypedDict):
    cdr_bucket: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The S3 bucket that stores the Voice Connector's call detail records.</p>"""


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
