"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#ContentType``."""

from typing import Literal, TypeAlias, cast

ContentType: TypeAlias = Literal[
    "application/json",
    "application/xml",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentType) -> str:
    return value


def deserialize_json(data: str) -> ContentType:
    return cast(ContentType, data)
