"""Generated from Smithy shape ``com.amazonaws.entityresolution#StatementActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.statement_action

StatementActionList: TypeAlias = list[
    "aws_sdk_entityresolution.types.statement_action.StatementAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: StatementActionList) -> list:
    return list(value)


def deserialize_json(data: list) -> StatementActionList:
    return list(data)
