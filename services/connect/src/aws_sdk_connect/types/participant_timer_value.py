"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.participant_timer_action
    import aws_sdk_connect.types.participant_timer_duration_in_minutes


class _ParticipantTimerValue_ParticipantTimerAction(TypedDict):
    ParticipantTimerAction: (
        "aws_sdk_connect.types.participant_timer_action.ParticipantTimerAction"
    )


class _ParticipantTimerValue_ParticipantTimerDurationInMinutes(TypedDict):
    ParticipantTimerDurationInMinutes: "aws_sdk_connect.types.participant_timer_duration_in_minutes.ParticipantTimerDurationInMinutes"


ParticipantTimerValue: TypeAlias = (
    _ParticipantTimerValue_ParticipantTimerAction
    | _ParticipantTimerValue_ParticipantTimerDurationInMinutes
)


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerValue) -> dict:
    if "ParticipantTimerAction" in value:
        import aws_sdk_connect.types.participant_timer_action

        return {
            "ParticipantTimerAction": aws_sdk_connect.types.participant_timer_action.serialize_json(
                value["ParticipantTimerAction"]
            )
        }
    elif "ParticipantTimerDurationInMinutes" in value:
        return {
            "ParticipantTimerDurationInMinutes": value[
                "ParticipantTimerDurationInMinutes"
            ]
        }
    else:
        raise SerializationError("ParticipantTimerValue: no variant present")


def deserialize_json(data: dict) -> ParticipantTimerValue:
    if "ParticipantTimerAction" in data:
        import aws_sdk_connect.types.participant_timer_action

        return {
            "ParticipantTimerAction": aws_sdk_connect.types.participant_timer_action.deserialize_json(
                data["ParticipantTimerAction"]
            )
        }
    elif "ParticipantTimerDurationInMinutes" in data:
        return {
            "ParticipantTimerDurationInMinutes": data[
                "ParticipantTimerDurationInMinutes"
            ]
        }
    else:
        raise DeserializationError("ParticipantTimerValue: no recognized variant key")
