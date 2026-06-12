"""Generated from Smithy shape ``com.amazonaws.lakeformation#WorkUnitRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.work_unit_range

WorkUnitRangeList: TypeAlias = list[
    "aws_sdk_lakeformation.types.work_unit_range.WorkUnitRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkUnitRangeList) -> list:
    import aws_sdk_lakeformation.types.work_unit_range

    out: list = []
    for item in value:
        out.append(aws_sdk_lakeformation.types.work_unit_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkUnitRangeList:
    import aws_sdk_lakeformation.types.work_unit_range

    out: WorkUnitRangeList = []
    for item in data:
        out.append(aws_sdk_lakeformation.types.work_unit_range.deserialize_json(item))
    return out
