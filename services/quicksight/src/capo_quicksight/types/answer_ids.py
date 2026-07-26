"""Generated from Smithy shape ``com.amazonaws.quicksight#AnswerIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.answer_id

AnswerIds: TypeAlias = list["capo_quicksight.types.answer_id.AnswerId"]


# --- restJson1 ser/de ---
def serialize_json(value: AnswerIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AnswerIds:
    return list(data)
