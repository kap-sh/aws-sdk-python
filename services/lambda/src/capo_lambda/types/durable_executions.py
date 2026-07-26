"""Generated from Smithy shape ``com.amazonaws.lambda#DurableExecutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.execution

DurableExecutions: TypeAlias = list["capo_lambda.types.execution.Execution"]


# --- restJson1 ser/de ---
def serialize_json(value: DurableExecutions) -> list:
    import capo_lambda.types.execution

    out: list = []
    for item in value:
        out.append(capo_lambda.types.execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> DurableExecutions:
    import capo_lambda.types.execution

    out: DurableExecutions = []
    for item in data:
        out.append(capo_lambda.types.execution.deserialize_json(item))
    return out
