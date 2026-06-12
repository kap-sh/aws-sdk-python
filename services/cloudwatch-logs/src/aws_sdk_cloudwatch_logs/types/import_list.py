"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import

ImportList: TypeAlias = list["aws_sdk_cloudwatch_logs.types.import.Import"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportList) -> list:
    import aws_sdk_cloudwatch_logs.types.import
    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_logs.types.import.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImportList:
    import aws_sdk_cloudwatch_logs.types.import
    out: ImportList = []
    for item in data:
        out.append(aws_sdk_cloudwatch_logs.types.import.deserialize_aws_json_1_1(item))
    return out