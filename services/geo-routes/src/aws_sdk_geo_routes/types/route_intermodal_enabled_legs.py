"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalEnabledLegs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteIntermodalEnabledLegs: TypeAlias = Literal[
    "FirstLeg",
    "LastLeg",
    "EntireRoute",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FirstLeg",
        "LastLeg",
        "EntireRoute",
        "None",
    )
)


def serialize_json(value: RouteIntermodalEnabledLegs) -> str:
    return value


def deserialize_json(data: str) -> RouteIntermodalEnabledLegs:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteIntermodalEnabledLegs value: {data!r}"
        )
    return cast(RouteIntermodalEnabledLegs, data)
