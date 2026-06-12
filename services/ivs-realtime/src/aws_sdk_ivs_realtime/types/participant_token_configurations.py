"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_token_configuration

ParticipantTokenConfigurations: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.participant_token_configuration.ParticipantTokenConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenConfigurations) -> list:
    import aws_sdk_ivs_realtime.types.participant_token_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ivs_realtime.types.participant_token_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ParticipantTokenConfigurations:
    import aws_sdk_ivs_realtime.types.participant_token_configuration

    out: ParticipantTokenConfigurations = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.participant_token_configuration.deserialize_json(
                item
            )
        )
    return out
