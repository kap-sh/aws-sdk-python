"""Generated from Smithy shape ``com.amazonaws.workdocs#RolePermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

RolePermissionType: TypeAlias = Literal[
    "DIRECT",
    "INHERITED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT",
        "INHERITED",
    )
)


def serialize_json(value: RolePermissionType) -> str:
    return value


def deserialize_json(data: str) -> RolePermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RolePermissionType value: {data!r}")
    return cast(RolePermissionType, data)
