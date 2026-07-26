"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_mapper_segment

NetworkMigrationMapperSegmentsList: TypeAlias = list[
    "capo_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegmentsList) -> list:
    import capo_mgn.types.network_migration_mapper_segment

    out: list = []
    for item in value:
        out.append(capo_mgn.types.network_migration_mapper_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkMigrationMapperSegmentsList:
    import capo_mgn.types.network_migration_mapper_segment

    out: NetworkMigrationMapperSegmentsList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_mapper_segment.deserialize_json(item)
        )
    return out
