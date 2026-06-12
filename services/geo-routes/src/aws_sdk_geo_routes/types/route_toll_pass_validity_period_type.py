"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPassValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTollPassValidityPeriodType: TypeAlias = Literal[
    "Annual",
    "Days",
    "ExtendedAnnual",
    "Minutes",
    "Months",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Annual",
        "Days",
        "ExtendedAnnual",
        "Minutes",
        "Months",
    )
)


def serialize_json(value: RouteTollPassValidityPeriodType) -> str:
    return value


def deserialize_json(data: str) -> RouteTollPassValidityPeriodType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTollPassValidityPeriodType value: {data!r}"
        )
    return cast(RouteTollPassValidityPeriodType, data)
