"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ProcessedInputRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.processed_input_record

ProcessedInputRecords: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.processed_input_record.ProcessedInputRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessedInputRecords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProcessedInputRecords:
    return list(data)
