"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_item

BatchGetSessionItems: TypeAlias = list[
    "capo_deadline.types.batch_get_session_item.BatchGetSessionItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionItems) -> list:
    import capo_deadline.types.batch_get_session_item

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_session_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetSessionItems:
    import capo_deadline.types.batch_get_session_item

    out: BatchGetSessionItems = []
    for item in data:
        out.append(capo_deadline.types.batch_get_session_item.deserialize_json(item))
    return out
