"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorIntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

VoiceConnectorIntegrationType: TypeAlias = Literal[
    "CONNECT_CALL_TRANSFER_CONNECTOR",
    "CONNECT_ANALYTICS_CONNECTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECT_CALL_TRANSFER_CONNECTOR",
        "CONNECT_ANALYTICS_CONNECTOR",
    )
)


def serialize_json(value: VoiceConnectorIntegrationType) -> str:
    return value


def deserialize_json(data: str) -> VoiceConnectorIntegrationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VoiceConnectorIntegrationType value: {data!r}"
        )
    return cast(VoiceConnectorIntegrationType, data)
