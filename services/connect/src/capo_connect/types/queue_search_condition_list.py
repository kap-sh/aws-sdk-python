"""Generated from Smithy shape ``com.amazonaws.connect#QueueSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.queue_search_criteria

QueueSearchConditionList: TypeAlias = list[
    "capo_connect.types.queue_search_criteria.QueueSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueSearchConditionList) -> list:
    import capo_connect.types.queue_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.queue_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueueSearchConditionList:
    import capo_connect.types.queue_search_criteria

    out: QueueSearchConditionList = []
    for item in data:
        out.append(capo_connect.types.queue_search_criteria.deserialize_json(item))
    return out
