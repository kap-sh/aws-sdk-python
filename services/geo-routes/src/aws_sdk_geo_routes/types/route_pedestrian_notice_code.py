"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoutePedestrianNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "Other",
    "ViolatedAvoidDirtRoad",
    "ViolatedAvoidTunnel",
    "ViolatedPedestrianOption",
    "ViolatedAvoidAreas",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccuratePolylineUnavailable",
        "Other",
        "ViolatedAvoidDirtRoad",
        "ViolatedAvoidTunnel",
        "ViolatedPedestrianOption",
        "ViolatedAvoidAreas",
    )
)


def serialize_json(value: RoutePedestrianNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutePedestrianNoticeCode value: {data!r}")
    return cast(RoutePedestrianNoticeCode, data)
