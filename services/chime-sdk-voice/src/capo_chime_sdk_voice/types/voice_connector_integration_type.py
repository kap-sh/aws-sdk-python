"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceConnectorIntegrationType``."""

from typing import Literal, TypeAlias, cast

VoiceConnectorIntegrationType: TypeAlias = Literal[
    "CONNECT_CALL_TRANSFER_CONNECTOR",
    "CONNECT_ANALYTICS_CONNECTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceConnectorIntegrationType) -> str:
    return value


def deserialize_json(data: str) -> VoiceConnectorIntegrationType:
    return cast(VoiceConnectorIntegrationType, data)
