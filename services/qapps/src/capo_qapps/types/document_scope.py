"""Generated from Smithy shape ``com.amazonaws.qapps#DocumentScope``."""

from typing import Literal, TypeAlias, cast

DocumentScope: TypeAlias = Literal[
    "APPLICATION",
    "SESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentScope) -> str:
    return value


def deserialize_json(data: str) -> DocumentScope:
    return cast(DocumentScope, data)
