"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_PAGINATION_TOKEN",
    "MALFORMED_REQUEST_PARAMETERS",
    "PAGINATION_LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_PAGINATION_TOKEN",
        "MALFORMED_REQUEST_PARAMETERS",
        "PAGINATION_LIMIT_EXCEEDED",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
