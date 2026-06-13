"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentsIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.segment_id

ListNetworkMigrationMapperSegmentsIDsFilter: TypeAlias = list[
    "aws_sdk_mgn.types.segment_id.SegmentID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentsIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationMapperSegmentsIDsFilter:
    return list(data)
