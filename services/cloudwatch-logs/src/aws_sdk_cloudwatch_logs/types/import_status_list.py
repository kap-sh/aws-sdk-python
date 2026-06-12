"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import_status

ImportStatusList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.import_status.ImportStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatusList) -> list:
    import aws_sdk_cloudwatch_logs.types.import_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImportStatusList:
    import aws_sdk_cloudwatch_logs.types.import_status

    out: ImportStatusList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(item)
        )
    return out
