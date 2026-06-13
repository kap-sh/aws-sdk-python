"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateSegments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_segment

StartNetworkMigrationMappingUpdateSegments: TypeAlias = list[
    "aws_sdk_mgn.types.start_network_migration_mapping_update_segment.StartNetworkMigrationMappingUpdateSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateSegments) -> list:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.start_network_migration_mapping_update_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartNetworkMigrationMappingUpdateSegments:
    import aws_sdk_mgn.types.start_network_migration_mapping_update_segment

    out: StartNetworkMigrationMappingUpdateSegments = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.start_network_migration_mapping_update_segment.deserialize_json(
                item
            )
        )
    return out
