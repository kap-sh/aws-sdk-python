"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteResponseNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteResponseNoticeCode: TypeAlias = Literal[
    "MainLanguageNotFound",
    "Other",
    "TravelTimeExceedsDriverWorkHours",
    "TransitDataUnavailable",
    "TransitRouteUnavailable",
    "NoTransitStationsFound",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MainLanguageNotFound",
        "Other",
        "TravelTimeExceedsDriverWorkHours",
        "TransitDataUnavailable",
        "TransitRouteUnavailable",
        "NoTransitStationsFound",
    )
)


def serialize_json(value: RouteResponseNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteResponseNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteResponseNoticeCode value: {data!r}")
    return cast(RouteResponseNoticeCode, data)
