"""Generated from Smithy shape ``com.amazonaws.drs#DescribeSourceServersRequestFiltersIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.source_server_id

DescribeSourceServersRequestFiltersIDs: TypeAlias = list[
    "capo_drs.types.source_server_id.SourceServerID"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceServersRequestFiltersIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeSourceServersRequestFiltersIDs:
    return list(data)
