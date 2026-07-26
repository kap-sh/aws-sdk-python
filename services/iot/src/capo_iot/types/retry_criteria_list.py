"""Generated from Smithy shape ``com.amazonaws.iot#RetryCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.retry_criteria

RetryCriteriaList: TypeAlias = list["capo_iot.types.retry_criteria.RetryCriteria"]


# --- restJson1 ser/de ---
def serialize_json(value: RetryCriteriaList) -> list:
    import capo_iot.types.retry_criteria

    out: list = []
    for item in value:
        out.append(capo_iot.types.retry_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetryCriteriaList:
    import capo_iot.types.retry_criteria

    out: RetryCriteriaList = []
    for item in data:
        out.append(capo_iot.types.retry_criteria.deserialize_json(item))
    return out
