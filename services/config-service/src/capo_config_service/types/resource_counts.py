"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.resource_count

ResourceCounts: TypeAlias = list[
    "capo_config_service.types.resource_count.ResourceCount"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceCounts) -> list:
    import capo_config_service.types.resource_count

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.resource_count.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceCounts:
    import capo_config_service.types.resource_count

    out: ResourceCounts = []
    for item in data:
        out.append(
            capo_config_service.types.resource_count.deserialize_aws_json_1_1(item)
        )
    return out
