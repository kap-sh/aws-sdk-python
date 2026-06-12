"""Generated from Smithy shape ``com.amazonaws.eventbridge#StartReplayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.replay_arn
    import aws_sdk_eventbridge.types.replay_state
    import aws_sdk_eventbridge.types.replay_state_reason
    import aws_sdk_eventbridge.types.timestamp


class StartReplayResponse(TypedDict):
    replay_arn: NotRequired["aws_sdk_eventbridge.types.replay_arn.ReplayArn"]
    """<p>The ARN of the replay.</p>"""
    state: NotRequired["aws_sdk_eventbridge.types.replay_state.ReplayState"]
    """<p>The state of the replay.</p>"""
    state_reason: NotRequired[
        "aws_sdk_eventbridge.types.replay_state_reason.ReplayStateReason"
    ]
    """<p>The reason that the replay is in the state.</p>"""
    replay_start_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>The time at which the replay started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplayResponse) -> dict:
    out: dict = {}
    if "replay_arn" in value:
        out["ReplayArn"] = value["replay_arn"]
    if "state" in value:
        import aws_sdk_eventbridge.types.replay_state

        out["State"] = aws_sdk_eventbridge.types.replay_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "replay_start_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["ReplayStartTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["replay_start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplayResponse:
    out: StartReplayResponse = {}  # type: ignore[typeddict-item]
    if "ReplayArn" in data:
        out["replay_arn"] = data["ReplayArn"]
    if "State" in data:
        import aws_sdk_eventbridge.types.replay_state

        out["state"] = aws_sdk_eventbridge.types.replay_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "ReplayStartTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["replay_start_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["ReplayStartTime"]
            )
        )
    return out
