"""Generated from Smithy shape ``com.amazonaws.eventbridge#CancelReplayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.replay_name


class CancelReplayRequest(TypedDict):
    replay_name: "aws_sdk_eventbridge.types.replay_name.ReplayName"
    """<p>The name of the replay to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplayRequest) -> dict:
    out: dict = {}
    out["ReplayName"] = value["replay_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplayRequest:
    out: CancelReplayRequest = {}  # type: ignore[typeddict-item]
    if "ReplayName" in data:
        out["replay_name"] = data["ReplayName"]
    else:
        raise DeserializationError("CancelReplayRequest.replay_name required")
    return out
