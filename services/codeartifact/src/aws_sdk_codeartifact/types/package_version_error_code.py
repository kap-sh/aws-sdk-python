"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageVersionErrorCode: TypeAlias = Literal[
    "ALREADY_EXISTS",
    "MISMATCHED_REVISION",
    "MISMATCHED_STATUS",
    "NOT_ALLOWED",
    "NOT_FOUND",
    "SKIPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALREADY_EXISTS",
        "MISMATCHED_REVISION",
        "MISMATCHED_STATUS",
        "NOT_ALLOWED",
        "NOT_FOUND",
        "SKIPPED",
    )
)


def serialize_json(value: PackageVersionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionErrorCode value: {data!r}")
    return cast(PackageVersionErrorCode, data)
