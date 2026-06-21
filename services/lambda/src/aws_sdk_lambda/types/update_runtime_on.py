"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateRuntimeOn``."""

from typing import Literal, TypeAlias, cast

UpdateRuntimeOn: TypeAlias = Literal[
    "Auto",
    "Manual",
    "FunctionUpdate",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuntimeOn) -> str:
    return value


def deserialize_json(data: str) -> UpdateRuntimeOn:
    return cast(UpdateRuntimeOn, data)
