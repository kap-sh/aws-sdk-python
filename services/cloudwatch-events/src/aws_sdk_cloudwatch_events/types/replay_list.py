"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ReplayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.replay

ReplayList: TypeAlias = list["aws_sdk_cloudwatch_events.types.replay.Replay"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayList) -> list:
    import aws_sdk_cloudwatch_events.types.replay

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_events.types.replay.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReplayList:
    import aws_sdk_cloudwatch_events.types.replay

    out: ReplayList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.replay.deserialize_aws_json_1_1(item)
        )
    return out
