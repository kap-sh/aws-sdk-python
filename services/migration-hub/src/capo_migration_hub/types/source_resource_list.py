"""Generated from Smithy shape ``com.amazonaws.migrationhub#SourceResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub.types.source_resource

SourceResourceList: TypeAlias = list[
    "capo_migration_hub.types.source_resource.SourceResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceResourceList) -> list:
    import capo_migration_hub.types.source_resource

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub.types.source_resource.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceResourceList:
    import capo_migration_hub.types.source_resource

    out: SourceResourceList = []
    for item in data:
        out.append(
            capo_migration_hub.types.source_resource.deserialize_aws_json_1_1(item)
        )
    return out
