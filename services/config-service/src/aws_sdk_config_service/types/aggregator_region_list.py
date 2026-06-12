"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.string

AggregatorRegionList: TypeAlias = list["aws_sdk_config_service.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatorRegionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AggregatorRegionList:
    return list(data)
