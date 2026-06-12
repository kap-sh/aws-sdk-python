"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

PackageVersionStatus: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PUBLISHED",
        "DEPRECATED",
    )
)


def serialize_json(value: PackageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionStatus value: {data!r}")
    return cast(PackageVersionStatus, data)
