"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSourceDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_description

ReferenceDataSourceDescriptions: TypeAlias = list[
    "aws_sdk_kinesis_analytics_v2.types.reference_data_source_description.ReferenceDataSourceDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceDescriptions) -> list:
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReferenceDataSourceDescriptions:
    import aws_sdk_kinesis_analytics_v2.types.reference_data_source_description

    out: ReferenceDataSourceDescriptions = []
    for item in data:
        out.append(
            aws_sdk_kinesis_analytics_v2.types.reference_data_source_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
