"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.resource_key

ResourceKeys: TypeAlias = list["capo_config_service.types.resource_key.ResourceKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceKeys) -> list:
    import capo_config_service.types.resource_key

    out: list = []
    for item in value:
        out.append(capo_config_service.types.resource_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceKeys:
    import capo_config_service.types.resource_key

    out: ResourceKeys = []
    for item in data:
        out.append(
            capo_config_service.types.resource_key.deserialize_aws_json_1_1(item)
        )
    return out
