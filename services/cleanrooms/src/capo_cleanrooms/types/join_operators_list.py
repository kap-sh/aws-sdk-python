"""Generated from Smithy shape ``com.amazonaws.cleanrooms#JoinOperatorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.join_operator

JoinOperatorsList: TypeAlias = list["capo_cleanrooms.types.join_operator.JoinOperator"]


# --- restJson1 ser/de ---
def serialize_json(value: JoinOperatorsList) -> list:
    return list(value)


def deserialize_json(data: list) -> JoinOperatorsList:
    return list(data)
