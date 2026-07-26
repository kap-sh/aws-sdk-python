"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormActionType``."""

from typing import Literal, TypeAlias, cast

FormActionType: TypeAlias = Literal[
    "create",
    "update",
]


# --- restJson1 ser/de ---
def serialize_json(value: FormActionType) -> str:
    return value


def deserialize_json(data: str) -> FormActionType:
    return cast(FormActionType, data)
