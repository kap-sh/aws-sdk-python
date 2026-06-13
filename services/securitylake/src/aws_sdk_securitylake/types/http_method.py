"""Generated from Smithy shape ``com.amazonaws.securitylake#HttpMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securitylake.errors import DeserializationError

HttpMethod: TypeAlias = Literal[
    "POST",
    "PUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POST",
        "PUT",
    )
)


def serialize_json(value: HttpMethod) -> str:
    return value


def deserialize_json(data: str) -> HttpMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpMethod value: {data!r}")
    return cast(HttpMethod, data)
