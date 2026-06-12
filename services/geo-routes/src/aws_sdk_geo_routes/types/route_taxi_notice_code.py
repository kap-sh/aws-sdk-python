"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "Other",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccuratePolylineUnavailable",
        "Other",
    )
)


def serialize_json(value: RouteTaxiNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTaxiNoticeCode value: {data!r}")
    return cast(RouteTaxiNoticeCode, data)
