"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ParsedInputRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.parsed_input_record

ParsedInputRecords: TypeAlias = list[
    "capo_kinesis_analytics.types.parsed_input_record.ParsedInputRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParsedInputRecords) -> list:
    import capo_kinesis_analytics.types.parsed_input_record

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics.types.parsed_input_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParsedInputRecords:
    import capo_kinesis_analytics.types.parsed_input_record

    out: ParsedInputRecords = []
    for item in data:
        out.append(
            capo_kinesis_analytics.types.parsed_input_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
