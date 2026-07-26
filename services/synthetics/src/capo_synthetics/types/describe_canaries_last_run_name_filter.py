"""Generated from Smithy shape ``com.amazonaws.synthetics#DescribeCanariesLastRunNameFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.canary_name

DescribeCanariesLastRunNameFilter: TypeAlias = list[
    "capo_synthetics.types.canary_name.CanaryName"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCanariesLastRunNameFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> DescribeCanariesLastRunNameFilter:
    return list(data)
