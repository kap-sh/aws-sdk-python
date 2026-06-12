"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageGroupOriginRestrictionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

PackageGroupOriginRestrictionType: TypeAlias = Literal[
    "EXTERNAL_UPSTREAM",
    "INTERNAL_UPSTREAM",
    "PUBLISH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTERNAL_UPSTREAM",
        "INTERNAL_UPSTREAM",
        "PUBLISH",
    )
)


def serialize_json(value: PackageGroupOriginRestrictionType) -> str:
    return value


def deserialize_json(data: str) -> PackageGroupOriginRestrictionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PackageGroupOriginRestrictionType value: {data!r}"
        )
    return cast(PackageGroupOriginRestrictionType, data)
