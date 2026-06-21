"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNoticeCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteTransitNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitNoticeCode:
    return cast(RouteTransitNoticeCode, data)
