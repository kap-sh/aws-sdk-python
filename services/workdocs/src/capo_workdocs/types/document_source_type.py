"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentSourceType``."""

from typing import Literal, TypeAlias, cast

DocumentSourceType: TypeAlias = Literal[
    "ORIGINAL",
    "WITH_COMMENTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentSourceType) -> str:
    return value


def deserialize_json(data: str) -> DocumentSourceType:
    return cast(DocumentSourceType, data)
