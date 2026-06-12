"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestrictionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageGroupOriginRestrictionMode: TypeAlias = Literal[
    "ALLOW",
    "ALLOW_SPECIFIC_REPOSITORIES",
    "BLOCK",
    "INHERIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "ALLOW_SPECIFIC_REPOSITORIES",
        "BLOCK",
        "INHERIT",
    )
)


def serialize_json(value: PackageGroupOriginRestrictionMode) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupOriginRestrictionMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PackageGroupOriginRestrictionMode value: {data!r}"
        )
    return cast(PackageGroupOriginRestrictionMode, data)
