"""Generated from Smithy shape ``com.amazonaws.qbusiness#PermissionConditionOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PermissionConditionOperator: TypeAlias = Literal["StringEquals",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("StringEquals",))


def serialize_json(value: PermissionConditionOperator) -> str:
    return value


def deserialize_json(data: str) -> PermissionConditionOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PermissionConditionOperator value: {data!r}"
        )
    return cast(PermissionConditionOperator, data)
