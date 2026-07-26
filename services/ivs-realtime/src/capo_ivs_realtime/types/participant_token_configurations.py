"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token_configuration

ParticipantTokenConfigurations: TypeAlias = list[
    "capo_ivs_realtime.types.participant_token_configuration.ParticipantTokenConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenConfigurations) -> list:
    import capo_ivs_realtime.types.participant_token_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ivs_realtime.types.participant_token_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ParticipantTokenConfigurations:
    import capo_ivs_realtime.types.participant_token_configuration

    out: ParticipantTokenConfigurations = []
    for item in data:
        out.append(
            capo_ivs_realtime.types.participant_token_configuration.deserialize_json(
                item
            )
        )
    return out
