"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteResponseNoticeCode``."""

from typing import Literal, TypeAlias, cast

RouteResponseNoticeCode: TypeAlias = Literal[
    "MainLanguageNotFound",
    "Other",
    "TravelTimeExceedsDriverWorkHours",
    "TransitDataUnavailable",
    "TransitRouteUnavailable",
    "NoTransitStationsFound",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteResponseNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteResponseNoticeCode:
    return cast(RouteResponseNoticeCode, data)
