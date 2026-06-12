"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

"""<p>Permission granted on a share request.</p>"""
PermissionType: TypeAlias = Literal[
    "READONLY",
    "CONTRIBUTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READONLY",
        "CONTRIBUTOR",
    )
)


def serialize_json(value: PermissionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionType value: {data!r}")
    return cast(PermissionType, data)
