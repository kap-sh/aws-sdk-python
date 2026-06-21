"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UriPathType``."""

from typing import Literal, TypeAlias, cast

UriPathType: TypeAlias = Literal[
    "LEAF",
    "ROOT",
]


# --- restJson1 ser/de ---
def serialize_json(value: UriPathType) -> str:
    return value


def deserialize_json(data: str) -> UriPathType:
    return cast(UriPathType, data)
