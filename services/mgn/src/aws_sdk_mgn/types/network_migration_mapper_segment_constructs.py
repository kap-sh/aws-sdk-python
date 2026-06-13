"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegmentConstructs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct

NetworkMigrationMapperSegmentConstructs: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_mapper_segment_construct.NetworkMigrationMapperSegmentConstruct"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegmentConstructs) -> list:
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_mapper_segment_construct.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationMapperSegmentConstructs:
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct

    out: NetworkMigrationMapperSegmentConstructs = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_mapper_segment_construct.deserialize_json(
                item
            )
        )
    return out
