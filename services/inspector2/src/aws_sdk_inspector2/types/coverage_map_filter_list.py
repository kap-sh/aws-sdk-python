"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageMapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_map_filter

CoverageMapFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.coverage_map_filter.CoverageMapFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageMapFilterList) -> list:
    import aws_sdk_inspector2.types.coverage_map_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.coverage_map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageMapFilterList:
    import aws_sdk_inspector2.types.coverage_map_filter

    out: CoverageMapFilterList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.coverage_map_filter.deserialize_json(item))
    return out
