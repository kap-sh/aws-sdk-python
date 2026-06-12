"""Generated from Smithy shape ``com.amazonaws.ssm#CalendarNameOrARNList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.calendar_name_or_arn

CalendarNameOrARNList: TypeAlias = list[
    "aws_sdk_ssm.types.calendar_name_or_arn.CalendarNameOrARN"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalendarNameOrARNList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CalendarNameOrARNList:
    return list(data)
