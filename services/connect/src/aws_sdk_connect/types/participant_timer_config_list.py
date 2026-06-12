"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.participant_timer_configuration

ParticipantTimerConfigList: TypeAlias = list[
    "aws_sdk_connect.types.participant_timer_configuration.ParticipantTimerConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerConfigList) -> list:
    import aws_sdk_connect.types.participant_timer_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.participant_timer_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ParticipantTimerConfigList:
    import aws_sdk_connect.types.participant_timer_configuration

    out: ParticipantTimerConfigList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.participant_timer_configuration.deserialize_json(item)
        )
    return out
