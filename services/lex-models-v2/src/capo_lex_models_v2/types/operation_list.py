"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_models_v2.types.operation

OperationList: TypeAlias = list["capo_lex_models_v2.types.operation.Operation"]


# --- restJson1 ser/de ---
def serialize_json(value: OperationList) -> list:
    return list(value)


def deserialize_json(data: list) -> OperationList:
    return list(data)
