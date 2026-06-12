"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_token

ParticipantTokenList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.participant_token.ParticipantToken"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenList) -> list:
    import aws_sdk_ivs_realtime.types.participant_token

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.participant_token.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantTokenList:
    import aws_sdk_ivs_realtime.types.participant_token

    out: ParticipantTokenList = []
    for item in data:
        out.append(aws_sdk_ivs_realtime.types.participant_token.deserialize_json(item))
    return out
