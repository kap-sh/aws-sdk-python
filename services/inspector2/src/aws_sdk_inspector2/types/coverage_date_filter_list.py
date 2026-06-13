"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageDateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_date_filter

CoverageDateFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.coverage_date_filter.CoverageDateFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageDateFilterList) -> list:
    import aws_sdk_inspector2.types.coverage_date_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.coverage_date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageDateFilterList:
    import aws_sdk_inspector2.types.coverage_date_filter

    out: CoverageDateFilterList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.coverage_date_filter.deserialize_json(item))
    return out
