"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ReplayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.replay

ReplayList: TypeAlias = list["capo_cloudwatch_events.types.replay.Replay"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayList) -> list:
    import capo_cloudwatch_events.types.replay

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_events.types.replay.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReplayList:
    import capo_cloudwatch_events.types.replay

    out: ReplayList = []
    for item in data:
        out.append(capo_cloudwatch_events.types.replay.deserialize_aws_json_1_1(item))
    return out
