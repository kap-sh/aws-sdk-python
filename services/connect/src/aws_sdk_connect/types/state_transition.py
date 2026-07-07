"""Generated from Smithy shape ``com.amazonaws.connect#StateTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.participant_state
    import aws_sdk_connect.types.timestamp


class StateTransition(TypedDict, closed=True):
    state: NotRequired["aws_sdk_connect.types.participant_state.ParticipantState"]
    """<p>The state of the transition.</p>"""
    state_start_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the state started in UTC time.</p>"""
    state_end_timestamp: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The date and time when the state ended in UTC time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StateTransition) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_connect.types.participant_state

        out["State"] = aws_sdk_connect.types.participant_state.serialize_json(
            value["state"]
        )
    if "state_start_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StateStartTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["state_start_timestamp"]
        )
    if "state_end_timestamp" in value:
        import aws_sdk_connect.types.timestamp

        out["StateEndTimestamp"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["state_end_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> StateTransition:
    out: StateTransition = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_connect.types.participant_state

        out["state"] = aws_sdk_connect.types.participant_state.deserialize_json(
            data["State"]
        )
    if "StateStartTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["state_start_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StateStartTimestamp"]
        )
    if "StateEndTimestamp" in data:
        import aws_sdk_connect.types.timestamp

        out["state_end_timestamp"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StateEndTimestamp"]
        )
    return out
