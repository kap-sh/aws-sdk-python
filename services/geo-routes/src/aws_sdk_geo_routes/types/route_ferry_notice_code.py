"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryNoticeCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteFerryNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryNoticeCode:
    return cast(RouteFerryNoticeCode, data)
