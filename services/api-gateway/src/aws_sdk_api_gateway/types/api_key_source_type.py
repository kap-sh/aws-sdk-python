"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeySourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

ApiKeySourceType: TypeAlias = Literal[
    "HEADER",
    "AUTHORIZER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEADER",
        "AUTHORIZER",
    )
)


def serialize_json(value: ApiKeySourceType) -> str:
    return value


def deserialize_json(data: str) -> ApiKeySourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiKeySourceType value: {data!r}")
    return cast(ApiKeySourceType, data)
