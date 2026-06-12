"""Generated from Smithy shape ``com.amazonaws.connect#FlowModuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

FlowModuleType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MCP",))


def serialize_json(value: FlowModuleType) -> str:
    return value


def deserialize_json(data: str) -> FlowModuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowModuleType value: {data!r}")
    return cast(FlowModuleType, data)
