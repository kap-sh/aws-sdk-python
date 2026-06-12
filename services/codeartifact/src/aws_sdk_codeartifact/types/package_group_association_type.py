"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupAssociationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageGroupAssociationType: TypeAlias = Literal[
    "STRONG",
    "WEAK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRONG",
        "WEAK",
    )
)


def serialize_json(value: PackageGroupAssociationType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupAssociationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PackageGroupAssociationType value: {data!r}"
        )
    return cast(PackageGroupAssociationType, data)
