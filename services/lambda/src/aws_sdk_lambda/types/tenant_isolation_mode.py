"""Generated from Smithy shape ``com.amazonaws.lambda#TenantIsolationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

TenantIsolationMode: TypeAlias = Literal["PER_TENANT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PER_TENANT",))


def serialize_json(value: TenantIsolationMode) -> str:
    return value


def deserialize_json(data: str) -> TenantIsolationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TenantIsolationMode value: {data!r}")
    return cast(TenantIsolationMode, data)
