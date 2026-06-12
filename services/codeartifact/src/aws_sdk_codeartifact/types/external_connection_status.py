"""Generated from Smithy shape ``com.amazonaws.codeartifact#ExternalConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

ExternalConnectionStatus: TypeAlias = Literal["Available",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Available",))


def serialize_json(value: ExternalConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExternalConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalConnectionStatus value: {data!r}")
    return cast(ExternalConnectionStatus, data)
