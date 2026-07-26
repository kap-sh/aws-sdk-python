"""Generated from Smithy shape ``com.amazonaws.lakeformation#WorkUnitRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.work_unit_range

WorkUnitRangeList: TypeAlias = list[
    "capo_lakeformation.types.work_unit_range.WorkUnitRange"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkUnitRangeList) -> list:
    import capo_lakeformation.types.work_unit_range

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.work_unit_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> WorkUnitRangeList:
    import capo_lakeformation.types.work_unit_range

    out: WorkUnitRangeList = []
    for item in data:
        out.append(capo_lakeformation.types.work_unit_range.deserialize_json(item))
    return out
