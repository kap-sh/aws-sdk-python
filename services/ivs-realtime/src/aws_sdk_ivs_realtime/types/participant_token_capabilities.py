"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_token_capability

ParticipantTokenCapabilities: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.participant_token_capability.ParticipantTokenCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenCapabilities) -> list:
    return list(value)


def deserialize_json(data: list) -> ParticipantTokenCapabilities:
    return list(data)
