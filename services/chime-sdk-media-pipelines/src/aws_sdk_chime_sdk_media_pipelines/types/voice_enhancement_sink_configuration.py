"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceEnhancementSinkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.boolean


class VoiceEnhancementSinkConfiguration(TypedDict, closed=True):
    disabled: "aws_sdk_chime_sdk_media_pipelines.types.boolean.Boolean"
    """<p>Disables the <code>VoiceEnhancementSinkConfiguration</code> element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementSinkConfiguration) -> dict:
    out: dict = {}
    out["Disabled"] = value.get("disabled", False)
    return out


def deserialize_json(data: dict) -> VoiceEnhancementSinkConfiguration:
    out: VoiceEnhancementSinkConfiguration = {}  # type: ignore[typeddict-item]
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    else:
        out["disabled"] = False
    return out
