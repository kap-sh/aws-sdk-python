"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSourceDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.reference_data_source_description

ReferenceDataSourceDescriptions: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.reference_data_source_description.ReferenceDataSourceDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceDescriptions) -> list:
    import capo_kinesis_analytics_v2.types.reference_data_source_description

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReferenceDataSourceDescriptions:
    import capo_kinesis_analytics_v2.types.reference_data_source_description

    out: ReferenceDataSourceDescriptions = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
