"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructsIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.construct_id

ListNetworkMigrationMapperSegmentConstructsIDsFilter: TypeAlias = list[
    "capo_mgn.types.construct_id.ConstructID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentConstructsIDsFilter) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> ListNetworkMigrationMapperSegmentConstructsIDsFilter:
    return list(data)
