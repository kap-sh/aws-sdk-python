"""Generated from Smithy shape ``com.amazonaws.lambda#OperationAction``."""

from typing import Literal, TypeAlias, cast

OperationAction: TypeAlias = Literal[
    "START",
    "SUCCEED",
    "FAIL",
    "RETRY",
    "CANCEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationAction) -> str:
    return value


def deserialize_json(data: str) -> OperationAction:
    return cast(OperationAction, data)
