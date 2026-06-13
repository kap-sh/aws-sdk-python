"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_string_filter

CoverageStringFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.coverage_string_filter.CoverageStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStringFilterList) -> list:
    import aws_sdk_inspector2.types.coverage_string_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.coverage_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageStringFilterList:
    import aws_sdk_inspector2.types.coverage_string_filter

    out: CoverageStringFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.coverage_string_filter.deserialize_json(item)
        )
    return out
