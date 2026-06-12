"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

OtaProtocol: TypeAlias = Literal["HTTP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HTTP",))


def serialize_json(value: OtaProtocol) -> str:
    return value


def deserialize_json(data: str) -> OtaProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OtaProtocol value: {data!r}")
    return cast(OtaProtocol, data)
