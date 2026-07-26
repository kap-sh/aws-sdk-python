"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ProcessedInputRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.processed_input_record

ProcessedInputRecords: TypeAlias = list[
    "capo_kinesis_analytics.types.processed_input_record.ProcessedInputRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessedInputRecords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProcessedInputRecords:
    return list(data)
