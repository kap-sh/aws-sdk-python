"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionErrorCode``."""

from typing import Literal, TypeAlias, cast

PackageVersionErrorCode: TypeAlias = Literal[
    "ALREADY_EXISTS",
    "MISMATCHED_REVISION",
    "MISMATCHED_STATUS",
    "NOT_ALLOWED",
    "NOT_FOUND",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionErrorCode) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionErrorCode:
    return cast(PackageVersionErrorCode, data)
