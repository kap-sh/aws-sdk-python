"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaMechanism``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

OtaMechanism: TypeAlias = Literal["PUSH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PUSH",))


def serialize_json(value: OtaMechanism) -> str:
    return value


def deserialize_json(data: str) -> OtaMechanism:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtaMechanism value: {data!r}")
    return cast(OtaMechanism, data)
