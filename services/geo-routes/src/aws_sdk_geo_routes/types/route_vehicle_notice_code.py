"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeCode``."""

from typing import Literal, TypeAlias, cast

RouteVehicleNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "Other",
    "PotentialViolatedAvoidTollRoadUsage",
    "PotentialViolatedCarpoolUsage",
    "PotentialViolatedTurnRestrictionUsage",
    "PotentialViolatedVehicleRestrictionUsage",
    "PotentialViolatedZoneRestrictionUsage",
    "SeasonalClosure",
    "TollsDataTemporarilyUnavailable",
    "TollsDataUnavailable",
    "TollTransponder",
    "ViolatedAvoidControlledAccessHighway",
    "ViolatedAvoidDifficultTurns",
    "ViolatedAvoidDirtRoad",
    "ViolatedAvoidSeasonalClosure",
    "ViolatedAvoidTollRoad",
    "ViolatedAvoidTollTransponder",
    "ViolatedAvoidTruckRoadType",
    "ViolatedAvoidTunnel",
    "ViolatedAvoidUTurns",
    "ViolatedBlockedRoad",
    "ViolatedCarpool",
    "ViolatedEmergencyGate",
    "ViolatedStartDirection",
    "ViolatedTurnRestriction",
    "ViolatedVehicleRestriction",
    "ViolatedZoneRestriction",
    "TravelTimeExceedsDriverWorkHours",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleNoticeCode:
    return cast(RouteVehicleNoticeCode, data)
