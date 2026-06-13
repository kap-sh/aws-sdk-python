"""Generated from Smithy shape ``com.amazonaws.ssmsap#PermissionActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

PermissionActionType: TypeAlias = Literal["RESTORE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESTORE",))


def serialize_json(value: PermissionActionType) -> str:
    return value


def deserialize_json(data: str) -> PermissionActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PermissionActionType value: {data!r}")
    return cast(PermissionActionType, data)
