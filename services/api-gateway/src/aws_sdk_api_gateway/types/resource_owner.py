"""Generated from Smithy shape ``com.amazonaws.apigateway#ResourceOwner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

ResourceOwner: TypeAlias = Literal[
    "SELF",
    "OTHER_ACCOUNTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELF",
        "OTHER_ACCOUNTS",
    )
)


def serialize_json(value: ResourceOwner) -> str:
    return value


def deserialize_json(data: str) -> ResourceOwner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceOwner value: {data!r}")
    return cast(ResourceOwner, data)
