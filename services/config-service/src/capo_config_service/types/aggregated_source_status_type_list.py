"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceStatusTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.aggregated_source_status_type

AggregatedSourceStatusTypeList: TypeAlias = list[
    "capo_config_service.types.aggregated_source_status_type.AggregatedSourceStatusType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedSourceStatusTypeList) -> list:
    import capo_config_service.types.aggregated_source_status_type

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.aggregated_source_status_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregatedSourceStatusTypeList:
    import capo_config_service.types.aggregated_source_status_type

    out: AggregatedSourceStatusTypeList = []
    for item in data:
        out.append(
            capo_config_service.types.aggregated_source_status_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
