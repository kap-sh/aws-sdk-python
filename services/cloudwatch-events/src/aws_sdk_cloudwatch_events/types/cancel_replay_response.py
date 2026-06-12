"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CancelReplayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.replay_arn
    import aws_sdk_cloudwatch_events.types.replay_state
    import aws_sdk_cloudwatch_events.types.replay_state_reason


class CancelReplayResponse(TypedDict):
    replay_arn: NotRequired["aws_sdk_cloudwatch_events.types.replay_arn.ReplayArn"]
    """<p>The ARN of the replay to cancel.</p>"""
    state: NotRequired["aws_sdk_cloudwatch_events.types.replay_state.ReplayState"]
    """<p>The current state of the replay.</p>"""
    state_reason: NotRequired[
        "aws_sdk_cloudwatch_events.types.replay_state_reason.ReplayStateReason"
    ]
    """<p>The reason that the replay is in the current state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplayResponse) -> dict:
    out: dict = {}
    if "replay_arn" in value:
        out["ReplayArn"] = value["replay_arn"]
    if "state" in value:
        import aws_sdk_cloudwatch_events.types.replay_state

        out["State"] = (
            aws_sdk_cloudwatch_events.types.replay_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplayResponse:
    out: CancelReplayResponse = {}  # type: ignore[typeddict-item]
    if "ReplayArn" in data:
        out["replay_arn"] = data["ReplayArn"]
    if "State" in data:
        import aws_sdk_cloudwatch_events.types.replay_state

        out["state"] = (
            aws_sdk_cloudwatch_events.types.replay_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    return out
