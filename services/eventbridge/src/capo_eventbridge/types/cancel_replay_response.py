"""Generated from Smithy shape ``com.amazonaws.eventbridge#CancelReplayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.replay_arn
    import capo_eventbridge.types.replay_state
    import capo_eventbridge.types.replay_state_reason


class CancelReplayResponse(TypedDict, closed=True):
    replay_arn: NotRequired["capo_eventbridge.types.replay_arn.ReplayArn"]
    """<p>The ARN of the replay to cancel.</p>"""
    state: NotRequired["capo_eventbridge.types.replay_state.ReplayState"]
    """<p>The current state of the replay.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.replay_state_reason.ReplayStateReason"
    ]
    """<p>The reason that the replay is in the current state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplayResponse) -> dict:
    out: dict = {}
    if "replay_arn" in value:
        out["ReplayArn"] = value["replay_arn"]
    if "state" in value:
        import capo_eventbridge.types.replay_state

        out["State"] = capo_eventbridge.types.replay_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplayResponse:
    out: CancelReplayResponse = {}  # type: ignore[typeddict-item]
    if "ReplayArn" in data:
        out["replay_arn"] = data["ReplayArn"]
    if "State" in data:
        import capo_eventbridge.types.replay_state

        out["state"] = capo_eventbridge.types.replay_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    return out
