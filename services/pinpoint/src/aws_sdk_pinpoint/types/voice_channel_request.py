"""Generated from Smithy shape ``com.amazonaws.pinpoint#VoiceChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean


class VoiceChannelRequest(TypedDict):
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the voice channel for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceChannelRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> VoiceChannelRequest:
    out: VoiceChannelRequest = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
