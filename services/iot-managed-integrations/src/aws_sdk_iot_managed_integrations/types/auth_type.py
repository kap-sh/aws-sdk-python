"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

AuthType: TypeAlias = Literal["OAUTH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OAUTH",))


def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthType value: {data!r}")
    return cast(AuthType, data)
