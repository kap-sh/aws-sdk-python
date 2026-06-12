"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_summary

ParticipantList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.participant_summary.ParticipantSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantList) -> list:
    import aws_sdk_ivs_realtime.types.participant_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.participant_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantList:
    import aws_sdk_ivs_realtime.types.participant_summary

    out: ParticipantList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.participant_summary.deserialize_json(item)
        )
    return out
