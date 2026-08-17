"""Generated from Smithy shape ``com.amazonaws.lambda#ExecutionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.execution_status

ExecutionStatusList: TypeAlias = list[
    "capo_lambda.types.execution_status.ExecutionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatusList) -> list:
    import capo_lambda.types.execution_status

    out: list = []
    for item in value:
        out.append(capo_lambda.types.execution_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExecutionStatusList:
    import capo_lambda.types.execution_status

    out: ExecutionStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.execution_status.deserialize_json(item))
    return out
