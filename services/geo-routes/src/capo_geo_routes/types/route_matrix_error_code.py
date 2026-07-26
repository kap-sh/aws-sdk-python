"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteMatrixErrorCode) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixErrorCode:
    return cast(RouteMatrixErrorCode, data)
