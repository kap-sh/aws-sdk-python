"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageVersionStatus: TypeAlias = Literal[
    "Published",
    "Unfinished",
    "Unlisted",
    "Archived",
    "Disposed",
    "Deleted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Published",
        "Unfinished",
        "Unlisted",
        "Archived",
        "Disposed",
        "Deleted",
    )
)


def serialize_json(value: PackageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionStatus value: {data!r}")
    return cast(PackageVersionStatus, data)
