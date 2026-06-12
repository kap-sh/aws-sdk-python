"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#VoiceAnalyticsConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

VoiceAnalyticsConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: VoiceAnalyticsConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> VoiceAnalyticsConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VoiceAnalyticsConfigurationStatus value: {data!r}"
        )
    return cast(VoiceAnalyticsConfigurationStatus, data)
