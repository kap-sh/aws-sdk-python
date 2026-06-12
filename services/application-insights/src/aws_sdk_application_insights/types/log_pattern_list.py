"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.log_pattern

LogPatternList: TypeAlias = list[
    "aws_sdk_application_insights.types.log_pattern.LogPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogPatternList) -> list:
    import aws_sdk_application_insights.types.log_pattern

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_insights.types.log_pattern.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogPatternList:
    import aws_sdk_application_insights.types.log_pattern

    out: LogPatternList = []
    for item in data:
        out.append(
            aws_sdk_application_insights.types.log_pattern.deserialize_aws_json_1_1(
                item
            )
        )
    return out
