"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructTypesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapper_segment_construct_type

ListNetworkMigrationMapperSegmentConstructTypesFilter: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_mapper_segment_construct_type.NetworkMigrationMapperSegmentConstructType"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: ListNetworkMigrationMapperSegmentConstructTypesFilter,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ListNetworkMigrationMapperSegmentConstructTypesFilter:
    return list(data)
