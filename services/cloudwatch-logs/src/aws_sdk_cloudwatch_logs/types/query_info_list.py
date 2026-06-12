"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.query_info

QueryInfoList: TypeAlias = list["aws_sdk_cloudwatch_logs.types.query_info.QueryInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryInfoList) -> list:
    import aws_sdk_cloudwatch_logs.types.query_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.query_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryInfoList:
    import aws_sdk_cloudwatch_logs.types.query_info

    out: QueryInfoList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.query_info.deserialize_aws_json_1_1(item)
        )
    return out
