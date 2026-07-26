"""Generated from Smithy shape ``com.amazonaws.connect#StateTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.participant_state
    import capo_connect.types.timestamp


class StateTransition(TypedDict, closed=True):
    state: NotRequired["capo_connect.types.participant_state.ParticipantState"]
    """<p>The state of the transition.</p>"""
    state_start_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the state started in UTC time.</p>"""
    state_end_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the state ended in UTC time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StateTransition) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_connect.types.participant_state

        out["State"] = capo_connect.types.participant_state.serialize_json(
            value["state"]
        )
    if "state_start_timestamp" in value:
        import capo_connect.types.timestamp

        out["StateStartTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["state_start_timestamp"]
        )
    if "state_end_timestamp" in value:
        import capo_connect.types.timestamp

        out["StateEndTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["state_end_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> StateTransition:
    out: StateTransition = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_connect.types.participant_state

        out["state"] = capo_connect.types.participant_state.deserialize_json(
            data["State"]
        )
    if "StateStartTimestamp" in data:
        import capo_connect.types.timestamp

        out["state_start_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["StateStartTimestamp"]
        )
    if "StateEndTimestamp" in data:
        import capo_connect.types.timestamp

        out["state_end_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["StateEndTimestamp"]
        )
    return out
