"""Generated from Smithy shape ``com.amazonaws.amplify#SourceUrlType``."""

from typing import Literal, TypeAlias, cast

SourceUrlType: TypeAlias = Literal[
    "ZIP",
    "BUCKET_PREFIX",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceUrlType) -> str:
    return value


def deserialize_json(data: str) -> SourceUrlType:
    return cast(SourceUrlType, data)
