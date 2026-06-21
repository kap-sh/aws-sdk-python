"""Generated from Smithy shape ``com.amazonaws.workdocs#ResponseItemType``."""

from typing import Literal, TypeAlias, cast

ResponseItemType: TypeAlias = Literal[
    "DOCUMENT",
    "FOLDER",
    "COMMENT",
    "DOCUMENT_VERSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseItemType) -> str:
    return value


def deserialize_json(data: str) -> ResponseItemType:
    return cast(ResponseItemType, data)
