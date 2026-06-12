"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ParsedInputRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.parsed_input_record

ParsedInputRecords: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.parsed_input_record.ParsedInputRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParsedInputRecords) -> list:
    import aws_sdk_kinesis_analytics_v2.types.parsed_input_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.parsed_input_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParsedInputRecords:
    import aws_sdk_kinesis_analytics_v2.types.parsed_input_record

    out: ParsedInputRecords = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.parsed_input_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
