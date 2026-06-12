"""Generated from Smithy shape ``com.amazonaws.mediatailor#Method``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

Method: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
    )
)


def serialize_json(value: Method) -> str:
    return value


def deserialize_json(data: str) -> Method:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Method value: {data!r}")
    return cast(Method, data)
