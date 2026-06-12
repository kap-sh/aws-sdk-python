"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiKeysFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

ApiKeysFormat: TypeAlias = Literal["csv",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("csv",))


def serialize_json(value: ApiKeysFormat) -> str:
    return value


def deserialize_json(data: str) -> ApiKeysFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiKeysFormat value: {data!r}")
    return cast(ApiKeysFormat, data)
