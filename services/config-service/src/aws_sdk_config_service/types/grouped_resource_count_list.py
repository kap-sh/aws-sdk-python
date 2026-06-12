"""Generated from Smithy shape ``com.amazonaws.configservice#GroupedResourceCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.grouped_resource_count

GroupedResourceCountList: TypeAlias = list[
    "aws_sdk_config_service.types.grouped_resource_count.GroupedResourceCount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupedResourceCountList) -> list:
    import aws_sdk_config_service.types.grouped_resource_count

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.grouped_resource_count.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupedResourceCountList:
    import aws_sdk_config_service.types.grouped_resource_count

    out: GroupedResourceCountList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.grouped_resource_count.deserialize_aws_json_1_1(
                item
            )
        )
    return out
