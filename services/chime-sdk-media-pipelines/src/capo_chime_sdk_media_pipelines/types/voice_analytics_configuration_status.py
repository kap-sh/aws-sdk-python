"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceAnalyticsConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

VoiceAnalyticsConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceAnalyticsConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> VoiceAnalyticsConfigurationStatus:
    return cast(VoiceAnalyticsConfigurationStatus, data)
