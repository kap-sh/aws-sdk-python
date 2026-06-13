"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationCodeGenerationSegmentsIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.segment_id

ListNetworkMigrationCodeGenerationSegmentsIDsFilter: TypeAlias = list[
    "aws_sdk_mgn.types.segment_id.SegmentID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationCodeGenerationSegmentsIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationCodeGenerationSegmentsIDsFilter:
    return list(data)
