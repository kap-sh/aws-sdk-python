"""Generated from Smithy shape ``com.amazonaws.datazone#S3Permission``."""

from typing import Literal, TypeAlias, cast

S3Permission: TypeAlias = Literal[
    "READ",
    "WRITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3Permission) -> str:
    return value


def deserialize_json(data: str) -> S3Permission:
    return cast(S3Permission, data)
