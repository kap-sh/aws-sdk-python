"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesNameFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.canary_name

DescribeCanariesNameFilter: TypeAlias = list[
    "capo_synthetics.types.canary_name.CanaryName"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesNameFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeCanariesNameFilter:
    return list(data)
