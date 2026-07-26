"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.target

TargetList: TypeAlias = list["capo_cloudwatch_events.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetList) -> list:
    import capo_cloudwatch_events.types.target

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_events.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetList:
    import capo_cloudwatch_events.types.target

    out: TargetList = []
    for item in data:
        out.append(capo_cloudwatch_events.types.target.deserialize_aws_json_1_1(item))
    return out
