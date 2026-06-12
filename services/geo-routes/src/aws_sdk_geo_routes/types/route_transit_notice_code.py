"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "IntermediateStopsUnavailable",
    "NoSchedule",
    "Other",
    "PotentialViolatedVehicleRestrictionUsage",
    "ScheduledTimes",
    "SeasonalClosure",
    "ViolatedAvoidFerry",
    "ViolatedAvoidRailFerry",
    "ViolatedExcludedTransitMode",
    "ViolatedVehicleRestriction",
    "ViolatedAvoidAreas",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccuratePolylineUnavailable",
        "IntermediateStopsUnavailable",
        "NoSchedule",
        "Other",
        "PotentialViolatedVehicleRestrictionUsage",
        "ScheduledTimes",
        "SeasonalClosure",
        "ViolatedAvoidFerry",
        "ViolatedAvoidRailFerry",
        "ViolatedExcludedTransitMode",
        "ViolatedVehicleRestriction",
        "ViolatedAvoidAreas",
    )
)


def serialize_json(value: RouteTransitNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTransitNoticeCode value: {data!r}")
    return cast(RouteTransitNoticeCode, data)
