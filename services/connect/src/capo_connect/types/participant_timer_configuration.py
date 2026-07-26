"""Generated from Smithy shape ``com.amazonaws.connect#ParticipantTimerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.participant_timer_type
    import capo_connect.types.participant_timer_value
    import capo_connect.types.timer_eligible_participant_roles


class ParticipantTimerConfiguration(TypedDict, closed=True):
    participant_role: "capo_connect.types.timer_eligible_participant_roles.TimerEligibleParticipantRoles"
    """<p>The role of the participant in the chat conversation.</p>"""
    timer_type: "capo_connect.types.participant_timer_type.ParticipantTimerType"
    """<p>The type of timer. <code>IDLE</code> indicates the timer applies for considering a human chat participant as idle. <code>DISCONNECT_NONCUSTOMER</code> indicates the timer applies to automatically disconnecting a chat participant due to idleness.</p>"""
    timer_value: "capo_connect.types.participant_timer_value.ParticipantTimerValue"
    """<p>The value of the timer. Either the timer action (Unset to delete the timer), or the duration of the timer in minutes. Only one value can be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTimerConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.timer_eligible_participant_roles

    out["ParticipantRole"] = (
        capo_connect.types.timer_eligible_participant_roles.serialize_json(
            value["participant_role"]
        )
    )
    import capo_connect.types.participant_timer_type

    out["TimerType"] = capo_connect.types.participant_timer_type.serialize_json(
        value["timer_type"]
    )
    import capo_connect.types.participant_timer_value

    out["TimerValue"] = capo_connect.types.participant_timer_value.serialize_json(
        value["timer_value"]
    )
    return out


def deserialize_json(data: dict) -> ParticipantTimerConfiguration:
    out: ParticipantTimerConfiguration = {}  # type: ignore[typeddict-item]
    if "ParticipantRole" in data:
        import capo_connect.types.timer_eligible_participant_roles

        out["participant_role"] = (
            capo_connect.types.timer_eligible_participant_roles.deserialize_json(
                data["ParticipantRole"]
            )
        )
    else:
        raise DeserializationError(
            "ParticipantTimerConfiguration.participant_role required"
        )
    if "TimerType" in data:
        import capo_connect.types.participant_timer_type

        out["timer_type"] = capo_connect.types.participant_timer_type.deserialize_json(
            data["TimerType"]
        )
    else:
        raise DeserializationError("ParticipantTimerConfiguration.timer_type required")
    if "TimerValue" in data:
        import capo_connect.types.participant_timer_value

        out["timer_value"] = (
            capo_connect.types.participant_timer_value.deserialize_json(
                data["TimerValue"]
            )
        )
    else:
        raise DeserializationError("ParticipantTimerConfiguration.timer_value required")
    return out
