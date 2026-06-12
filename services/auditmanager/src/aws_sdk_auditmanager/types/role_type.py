"""Generated from Smithy shape ``com.amazonaws.auditmanager#RoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

RoleType: TypeAlias = Literal[
    "PROCESS_OWNER",
    "RESOURCE_OWNER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESS_OWNER",
        "RESOURCE_OWNER",
    )
)


def serialize_json(value: RoleType) -> str:
    return value


def deserialize_json(data: str) -> RoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoleType value: {data!r}")
    return cast(RoleType, data)
