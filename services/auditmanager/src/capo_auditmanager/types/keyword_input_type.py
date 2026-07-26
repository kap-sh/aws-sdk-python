"""Generated from Smithy shape ``com.amazonaws.auditmanager#KeywordInputType``."""

from typing import Literal, TypeAlias, cast

KeywordInputType: TypeAlias = Literal[
    "SELECT_FROM_LIST",
    "UPLOAD_FILE",
    "INPUT_TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: KeywordInputType) -> str:
    return value


def deserialize_json(data: str) -> KeywordInputType:
    return cast(KeywordInputType, data)
