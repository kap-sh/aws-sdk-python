"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.reference_data_source

ReferenceDataSources: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.reference_data_source.ReferenceDataSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSources) -> list:
    import capo_kinesis_analytics_v2.types.reference_data_source

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReferenceDataSources:
    import capo_kinesis_analytics_v2.types.reference_data_source

    out: ReferenceDataSources = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
