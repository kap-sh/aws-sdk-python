"""Generated from Smithy shape ``com.amazonaws.eventbridge#StartReplayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.replay_arn
    import capo_eventbridge.types.replay_state
    import capo_eventbridge.types.replay_state_reason
    import capo_eventbridge.types.timestamp


class StartReplayResponse(TypedDict, closed=True):
    replay_arn: NotRequired["capo_eventbridge.types.replay_arn.ReplayArn"]
    """<p>The ARN of the replay.</p>"""
    state: NotRequired["capo_eventbridge.types.replay_state.ReplayState"]
    """<p>The state of the replay.</p>"""
    state_reason: NotRequired[
        "capo_eventbridge.types.replay_state_reason.ReplayStateReason"
    ]
    """<p>The reason that the replay is in the state.</p>"""
    replay_start_time: NotRequired["capo_eventbridge.types.timestamp.Timestamp"]
    """<p>The time at which the replay started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplayResponse) -> dict:
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
    if "replay_start_time" in value:
        import capo_eventbridge.types.timestamp

        out["ReplayStartTime"] = (
            capo_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["replay_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplayResponse:
    out: StartReplayResponse = {}  # type: ignore[typeddict-item]
    if "ReplayArn" in data:
        out["replay_arn"] = data["ReplayArn"]
    if "State" in data:
        import capo_eventbridge.types.replay_state

        out["state"] = capo_eventbridge.types.replay_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "ReplayStartTime" in data:
        import capo_eventbridge.types.timestamp

        out["replay_start_time"] = (
            capo_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["ReplayStartTime"]
            )
        )
    return out
