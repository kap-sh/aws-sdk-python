"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PermissionModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

PermissionModelType: TypeAlias = Literal[
    "LegacyIAMUser",
    "RoleBased",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LegacyIAMUser",
        "RoleBased",
    )
)


def serialize_json(value: PermissionModelType) -> str:
    return value


def deserialize_json(data: str) -> PermissionModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionModelType value: {data!r}")
    return cast(PermissionModelType, data)
