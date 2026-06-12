"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

EndpointType: TypeAlias = Literal["LAMBDA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAMBDA",))


def serialize_json(value: EndpointType) -> str:
    return value


def deserialize_json(data: str) -> EndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointType value: {data!r}")
    return cast(EndpointType, data)
