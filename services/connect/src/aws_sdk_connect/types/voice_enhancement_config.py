"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.channel
    import aws_sdk_connect.types.voice_enhancement_mode


class VoiceEnhancementConfig(TypedDict):
    channel: "aws_sdk_connect.types.channel.Channel"
    """<p>The channel for this voice enhancement configuration. <b>Only <code>VOICE</code> is supported for this data type.</b> </p>"""
    voice_enhancement_mode: (
        "aws_sdk_connect.types.voice_enhancement_mode.VoiceEnhancementMode"
    )
    """<p>The voice enhancement mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.channel

    out["Channel"] = aws_sdk_connect.types.channel.serialize_json(value["channel"])
    import aws_sdk_connect.types.voice_enhancement_mode

    out["VoiceEnhancementMode"] = (
        aws_sdk_connect.types.voice_enhancement_mode.serialize_json(
            value["voice_enhancement_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> VoiceEnhancementConfig:
    out: VoiceEnhancementConfig = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        import aws_sdk_connect.types.channel

        out["channel"] = aws_sdk_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("VoiceEnhancementConfig.channel required")
    if "VoiceEnhancementMode" in data:
        import aws_sdk_connect.types.voice_enhancement_mode

        out["voice_enhancement_mode"] = (
            aws_sdk_connect.types.voice_enhancement_mode.deserialize_json(
                data["VoiceEnhancementMode"]
            )
        )
    else:
        raise DeserializationError(
            "VoiceEnhancementConfig.voice_enhancement_mode required"
        )
    return out
