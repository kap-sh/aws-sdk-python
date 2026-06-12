"""Generated from Smithy shape ``com.amazonaws.glacier#CannedACL``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "private",
        "public-read",
        "public-read-write",
        "aws-exec-read",
        "authenticated-read",
        "bucket-owner-read",
        "bucket-owner-full-control",
    )
)


def serialize_json(value: CannedACL) -> str:
    return value


def deserialize_json(data: str) -> CannedACL:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CannedACL value: {data!r}")
    return cast(CannedACL, data)
