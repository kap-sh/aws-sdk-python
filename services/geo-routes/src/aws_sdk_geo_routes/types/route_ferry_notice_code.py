"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteFerryNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "NoSchedule",
    "Other",
    "ViolatedAvoidFerry",
    "ViolatedAvoidRailFerry",
    "SeasonalClosure",
    "PotentialViolatedVehicleRestrictionUsage",
    "ViolatedAvoidAreas",
    "ViolatedVehicleRestriction",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccuratePolylineUnavailable",
        "NoSchedule",
        "Other",
        "ViolatedAvoidFerry",
        "ViolatedAvoidRailFerry",
        "SeasonalClosure",
        "PotentialViolatedVehicleRestrictionUsage",
        "ViolatedAvoidAreas",
        "ViolatedVehicleRestriction",
    )
)


def serialize_json(value: RouteFerryNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteFerryNoticeCode value: {data!r}")
    return cast(RouteFerryNoticeCode, data)
