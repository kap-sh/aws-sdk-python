"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeReplayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.replay_name


class DescribeReplayRequest(TypedDict):
    replay_name: "aws_sdk_cloudwatch_events.types.replay_name.ReplayName"
    """<p>The name of the replay to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplayRequest) -> dict:
    out: dict = {}
    out["ReplayName"] = value["replay_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplayRequest:
    out: DescribeReplayRequest = {}  # type: ignore[typeddict-item]
    if "ReplayName" in data:
        out["replay_name"] = data["ReplayName"]
    else:
        raise DeserializationError("DescribeReplayRequest.replay_name required")
    return out
