"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_code_generation_segment

NetworkMigrationCodeGenerationSegmentsList: TypeAlias = list[
    "capo_mgn.types.network_migration_code_generation_segment.NetworkMigrationCodeGenerationSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationSegmentsList) -> list:
    import capo_mgn.types.network_migration_code_generation_segment

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_code_generation_segment.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationSegmentsList:
    import capo_mgn.types.network_migration_code_generation_segment

    out: NetworkMigrationCodeGenerationSegmentsList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_code_generation_segment.deserialize_json(
                item
            )
        )
    return out
