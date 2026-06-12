"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_parameter

QueryParameterList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.query_parameter.QueryParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryParameterList) -> list:
    import aws_sdk_cloudwatch_logs.types.query_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.query_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryParameterList:
    import aws_sdk_cloudwatch_logs.types.query_parameter

    out: QueryParameterList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.query_parameter.deserialize_aws_json_1_1(item)
        )
    return out
