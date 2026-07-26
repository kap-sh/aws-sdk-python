"""Generated from Smithy shape ``com.amazonaws.iot#AbortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.abort_criteria

AbortCriteriaList: TypeAlias = list["capo_iot.types.abort_criteria.AbortCriteria"]


# --- restJson1 ser/de ---
def serialize_json(value: AbortCriteriaList) -> list:
    import capo_iot.types.abort_criteria

    out: list = []
    for item in value:
        out.append(capo_iot.types.abort_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> AbortCriteriaList:
    import capo_iot.types.abort_criteria

    out: AbortCriteriaList = []
    for item in data:
        out.append(capo_iot.types.abort_criteria.deserialize_json(item))
    return out
