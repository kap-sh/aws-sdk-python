"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ReferenceDataSourceUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.reference_data_source_update

ReferenceDataSourceUpdates: TypeAlias = list[
    "aws_sdk_kinesis_analytics.types.reference_data_source_update.ReferenceDataSourceUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceUpdates) -> list:
    import aws_sdk_kinesis_analytics.types.reference_data_source_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics.types.reference_data_source_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReferenceDataSourceUpdates:
    import aws_sdk_kinesis_analytics.types.reference_data_source_update

    out: ReferenceDataSourceUpdates = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics.types.reference_data_source_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
