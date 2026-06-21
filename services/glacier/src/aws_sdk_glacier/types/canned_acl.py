"""Generated from Smithy shape ``com.amazonaws.glacier#CannedACL``."""

from typing import Literal, TypeAlias, cast

CannedACL: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
]


# --- restJson1 ser/de ---
def serialize_json(value: CannedACL) -> str:
    return value


def deserialize_json(data: str) -> CannedACL:
    return cast(CannedACL, data)
