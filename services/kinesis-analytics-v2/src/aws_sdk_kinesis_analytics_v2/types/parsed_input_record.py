"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ParsedInputRecord``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.parsed_input_record_field

ParsedInputRecord: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.parsed_input_record_field.ParsedInputRecordField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParsedInputRecord) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParsedInputRecord:
    return list(data)
