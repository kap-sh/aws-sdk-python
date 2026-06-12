"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RouteType: TypeAlias = Literal[
    "PROPAGATED",
    "STATIC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROPAGATED",
        "STATIC",
    )
)


def serialize_json(value: RouteType) -> str:
    return value


def deserialize_json(data: str) -> RouteType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteType value: {data!r}")
    return cast(RouteType, data)
