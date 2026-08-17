"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_field

LogGroupFieldList: TypeAlias = list[
    "capo_cloudwatch_logs.types.log_group_field.LogGroupField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupFieldList) -> list:
    import capo_cloudwatch_logs.types.log_group_field

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.log_group_field.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogGroupFieldList:
    import capo_cloudwatch_logs.types.log_group_field

    out: LogGroupFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.log_group_field.deserialize_aws_json_1_1(item)
        )
    return out
