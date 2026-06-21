"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResourceType``."""

from typing import Literal, TypeAlias, cast

SearchResourceType: TypeAlias = Literal[
    "FOLDER",
    "DOCUMENT",
    "COMMENT",
    "DOCUMENT_VERSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceType) -> str:
    return value


def deserialize_json(data: str) -> SearchResourceType:
    return cast(SearchResourceType, data)
