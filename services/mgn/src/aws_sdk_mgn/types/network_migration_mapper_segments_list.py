"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapper_segment

NetworkMigrationMapperSegmentsList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegmentsList) -> list:
    import aws_sdk_mgn.types.network_migration_mapper_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_mapper_segment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationMapperSegmentsList:
    import aws_sdk_mgn.types.network_migration_mapper_segment

    out: NetworkMigrationMapperSegmentsList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_mapper_segment.deserialize_json(item)
        )
    return out
