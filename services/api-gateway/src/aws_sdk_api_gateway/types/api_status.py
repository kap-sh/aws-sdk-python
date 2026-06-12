"""Generated from Smithy shape ``com.amazonaws.apigateway#ApiStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

ApiStatus: TypeAlias = Literal[
    "UPDATING",
    "AVAILABLE",
    "PENDING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "AVAILABLE",
        "PENDING",
        "FAILED",
    )
)


def serialize_json(value: ApiStatus) -> str:
    return value


def deserialize_json(data: str) -> ApiStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiStatus value: {data!r}")
    return cast(ApiStatus, data)
