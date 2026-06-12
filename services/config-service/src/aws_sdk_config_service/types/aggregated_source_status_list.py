"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregated_source_status

AggregatedSourceStatusList: TypeAlias = list[
    "aws_sdk_config_service.types.aggregated_source_status.AggregatedSourceStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedSourceStatusList) -> list:
    import aws_sdk_config_service.types.aggregated_source_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.aggregated_source_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregatedSourceStatusList:
    import aws_sdk_config_service.types.aggregated_source_status

    out: AggregatedSourceStatusList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.aggregated_source_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
