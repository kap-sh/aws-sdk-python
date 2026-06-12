"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#TokenEndpointAuthenticationScheme``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

TokenEndpointAuthenticationScheme: TypeAlias = Literal[
    "HTTP_BASIC",
    "REQUEST_BODY_CREDENTIALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_BASIC",
        "REQUEST_BODY_CREDENTIALS",
    )
)


def serialize_json(value: TokenEndpointAuthenticationScheme) -> str:
    return value


def deserialize_json(data: str) -> TokenEndpointAuthenticationScheme:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TokenEndpointAuthenticationScheme value: {data!r}"
        )
    return cast(TokenEndpointAuthenticationScheme, data)
