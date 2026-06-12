"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RuleResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.rule

RuleResponseList: TypeAlias = list["aws_sdk_cloudwatch_events.types.rule.Rule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleResponseList) -> list:
    import aws_sdk_cloudwatch_events.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_events.types.rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleResponseList:
    import aws_sdk_cloudwatch_events.types.rule

    out: RuleResponseList = []
    for item in data:
        out.append(aws_sdk_cloudwatch_events.types.rule.deserialize_aws_json_1_1(item))
    return out
