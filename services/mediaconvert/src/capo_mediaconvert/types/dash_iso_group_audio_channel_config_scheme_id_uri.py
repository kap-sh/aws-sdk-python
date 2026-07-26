"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashIsoGroupAudioChannelConfigSchemeIdUri``."""

from typing import Literal, TypeAlias, cast

"""Use this setting only when your audio codec is a Dolby one (AC3, EAC3, or Atmos) and your downstream workflow requires that your DASH manifest use the Dolby channel configuration tag, rather than the MPEG one. For example, you might need to use this to make dynamic ad insertion work. Specify which audio channel configuration scheme ID URI MediaConvert writes in your DASH manifest. Keep the default value, MPEG channel configuration, to have MediaConvert write this: urn:mpeg:mpegB:cicp:ChannelConfiguration. Choose Dolby channel configuration to have MediaConvert write this instead: tag:dolby.com,2014:dash:audio_channel_configuration:2011."""
DashIsoGroupAudioChannelConfigSchemeIdUri: TypeAlias = Literal[
    "MPEG_CHANNEL_CONFIGURATION",
    "DOLBY_CHANNEL_CONFIGURATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashIsoGroupAudioChannelConfigSchemeIdUri) -> str:
    return value


def deserialize_json(data: str) -> DashIsoGroupAudioChannelConfigSchemeIdUri:
    return cast(DashIsoGroupAudioChannelConfigSchemeIdUri, data)
