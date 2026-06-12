"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportBatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import_batch

ImportBatchList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.import_batch.ImportBatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportBatchList) -> list:
    import aws_sdk_cloudwatch_logs.types.import_batch

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.import_batch.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImportBatchList:
    import aws_sdk_cloudwatch_logs.types.import_batch

    out: ImportBatchList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.import_batch.deserialize_aws_json_1_1(item)
        )
    return out
