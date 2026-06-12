"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteMatrixErrorCode: TypeAlias = Literal[
    "NoMatch",
    "NoMatchDestination",
    "NoMatchOrigin",
    "NoRoute",
    "OutOfBounds",
    "OutOfBoundsDestination",
    "OutOfBoundsOrigin",
    "Other",
    "Violation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoMatch",
        "NoMatchDestination",
        "NoMatchOrigin",
        "NoRoute",
        "OutOfBounds",
        "OutOfBoundsDestination",
        "OutOfBoundsOrigin",
        "Other",
        "Violation",
    )
)


def serialize_json(value: RouteMatrixErrorCode) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteMatrixErrorCode value: {data!r}")
    return cast(RouteMatrixErrorCode, data)
