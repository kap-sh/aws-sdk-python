"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateActionType``."""

from typing import Literal, TypeAlias, cast

UpdateActionType: TypeAlias = Literal[
    "CREATE_OR_UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionType) -> str:
    return value


def deserialize_json(data: str) -> UpdateActionType:
    return cast(UpdateActionType, data)
