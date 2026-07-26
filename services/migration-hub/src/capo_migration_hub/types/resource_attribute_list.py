"""Generated from Smithy shape ``com.amazonaws.migrationhub#ResourceAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.resource_attribute

ResourceAttributeList: TypeAlias = list[
    "capo_migration_hub.types.resource_attribute.ResourceAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAttributeList) -> list:
    import capo_migration_hub.types.resource_attribute

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.resource_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceAttributeList:
    import capo_migration_hub.types.resource_attribute

    out: ResourceAttributeList = []
    for item in data:
        out.append(
            capo_migration_hub.types.resource_attribute.deserialize_aws_json_1_1(item)
        )
    return out
