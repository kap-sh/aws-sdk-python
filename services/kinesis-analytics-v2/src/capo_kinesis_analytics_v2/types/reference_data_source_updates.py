"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ReferenceDataSourceUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.reference_data_source_update

ReferenceDataSourceUpdates: TypeAlias = list[
    "capo_kinesis_analytics_v2.types.reference_data_source_update.ReferenceDataSourceUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDataSourceUpdates) -> list:
    import capo_kinesis_analytics_v2.types.reference_data_source_update

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReferenceDataSourceUpdates:
    import capo_kinesis_analytics_v2.types.reference_data_source_update

    out: ReferenceDataSourceUpdates = []
    for item in data:
        out.append(
            capo_kinesis_analytics_v2.types.reference_data_source_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
