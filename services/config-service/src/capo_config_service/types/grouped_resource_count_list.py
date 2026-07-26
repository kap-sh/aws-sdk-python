"""Generated from Smithy shape ``com.amazonaws.configservice#GroupedResourceCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.grouped_resource_count

GroupedResourceCountList: TypeAlias = list[
    "capo_config_service.types.grouped_resource_count.GroupedResourceCount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupedResourceCountList) -> list:
    import capo_config_service.types.grouped_resource_count

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.grouped_resource_count.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupedResourceCountList:
    import capo_config_service.types.grouped_resource_count

    out: GroupedResourceCountList = []
    for item in data:
        out.append(
            capo_config_service.types.grouped_resource_count.deserialize_aws_json_1_1(
                item
            )
        )
    return out
