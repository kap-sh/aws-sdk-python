"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeSourceServersRequestFiltersIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_server_id

DescribeSourceServersRequestFiltersIDs: TypeAlias = list[
    "aws_sdk_mgn.types.source_server_id.SourceServerID"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersRequestFiltersIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeSourceServersRequestFiltersIDs:
    return list(data)
