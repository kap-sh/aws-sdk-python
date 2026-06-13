"""Generated from Smithy shape ``com.amazonaws.drs#DescribeSourceNetworksRequestFiltersIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_network_id

DescribeSourceNetworksRequestFiltersIDs: TypeAlias = list[
    "aws_sdk_drs.types.source_network_id.SourceNetworkID"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceNetworksRequestFiltersIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeSourceNetworksRequestFiltersIDs:
    return list(data)
