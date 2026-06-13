"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_number_filter

CoverageNumberFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.coverage_number_filter.CoverageNumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageNumberFilterList) -> list:
    import aws_sdk_inspector2.types.coverage_number_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.coverage_number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageNumberFilterList:
    import aws_sdk_inspector2.types.coverage_number_filter

    out: CoverageNumberFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.coverage_number_filter.deserialize_json(item)
        )
    return out
