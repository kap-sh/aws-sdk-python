"""Generated from Smithy shape ``com.amazonaws.migrationhub#DiscoveredResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.discovered_resource

DiscoveredResourceList: TypeAlias = list[
    "capo_migration_hub.types.discovered_resource.DiscoveredResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResourceList) -> list:
    import capo_migration_hub.types.discovered_resource

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.discovered_resource.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DiscoveredResourceList:
    import capo_migration_hub.types.discovered_resource

    out: DiscoveredResourceList = []
    for item in data:
        out.append(
            capo_migration_hub.types.discovered_resource.deserialize_aws_json_1_1(item)
        )
    return out
