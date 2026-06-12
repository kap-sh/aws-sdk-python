"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RecordColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.record_column

RecordColumns: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.record_column.RecordColumn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordColumns) -> list:
    import aws_sdk_kinesis_analytics_v2.types.record_column

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.record_column.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecordColumns:
    import aws_sdk_kinesis_analytics_v2.types.record_column

    out: RecordColumns = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.record_column.deserialize_aws_json_1_1(
                item
            )
        )
    return out
