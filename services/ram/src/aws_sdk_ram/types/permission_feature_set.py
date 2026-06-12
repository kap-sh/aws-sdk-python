"""Generated from Smithy shape ``com.amazonaws.ram#PermissionFeatureSet``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ram.errors import DeserializationError

PermissionFeatureSet: TypeAlias = Literal[
    "CREATED_FROM_POLICY",
    "PROMOTING_TO_STANDARD",
    "STANDARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_FROM_POLICY",
        "PROMOTING_TO_STANDARD",
        "STANDARD",
    )
)


def serialize_json(value: PermissionFeatureSet) -> str:
    return value


def deserialize_json(data: str) -> PermissionFeatureSet:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionFeatureSet value: {data!r}")
    return cast(PermissionFeatureSet, data)
