"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_job_item

BatchGetJobItems: TypeAlias = list[
    "capo_deadline.types.batch_get_job_item.BatchGetJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobItems) -> list:
    import capo_deadline.types.batch_get_job_item

    out: list = []
    for item in value:
        out.append(capo_deadline.types.batch_get_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetJobItems:
    import capo_deadline.types.batch_get_job_item

    out: BatchGetJobItems = []
    for item in data:
        out.append(capo_deadline.types.batch_get_job_item.deserialize_json(item))
    return out
