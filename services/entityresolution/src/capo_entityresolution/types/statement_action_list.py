"""Generated from Smithy shape ``com.amazonaws.entityresolution#StatementActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.statement_action

StatementActionList: TypeAlias = list[
    "capo_entityresolution.types.statement_action.StatementAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatementActionList) -> list:
    return list(value)


def deserialize_json(data: list) -> StatementActionList:
    return list(data)
