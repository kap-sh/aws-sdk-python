"""Generated from Smithy shape ``com.amazonaws.iot#CannedAccessControlList``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CannedAccessControlList: TypeAlias = Literal[
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
    "log-delivery-write",
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
        "log-delivery-write",
    )
)


def serialize_json(value: CannedAccessControlList) -> str:
    return value


def deserialize_json(data: str) -> CannedAccessControlList:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CannedAccessControlList value: {data!r}")
    return cast(CannedAccessControlList, data)
