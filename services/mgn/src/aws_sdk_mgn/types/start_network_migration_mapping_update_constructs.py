"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateConstructs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_construct

StartNetworkMigrationMappingUpdateConstructs: TypeAlias = list[
    "aws_sdk_mgn.types.start_network_migration_mapping_update_construct.StartNetworkMigrationMappingUpdateConstruct"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateConstructs) -> list:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_construct

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.start_network_migration_mapping_update_construct.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartNetworkMigrationMappingUpdateConstructs:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_construct

    out: StartNetworkMigrationMappingUpdateConstructs = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.start_network_migration_mapping_update_construct.deserialize_json(
                item
            )
        )
    return out
