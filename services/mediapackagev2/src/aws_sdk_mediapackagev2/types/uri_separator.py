"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UriSeparator``."""

from typing import Literal, TypeAlias, cast

UriSeparator: TypeAlias = Literal[
    "UNDERSCORE",
    "HYPHEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: UriSeparator) -> str:
    return value


def deserialize_json(data: str) -> UriSeparator:
    return cast(UriSeparator, data)
