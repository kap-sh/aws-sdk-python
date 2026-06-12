"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#RawInputRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.raw_input_record

RawInputRecords: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.raw_input_record.RawInputRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RawInputRecords) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RawInputRecords:
    return list(data)
