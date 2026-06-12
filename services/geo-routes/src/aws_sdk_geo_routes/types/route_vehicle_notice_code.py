"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleNoticeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteVehicleNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleNoticeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteVehicleNoticeCode value: {data!r}")
    return cast(RouteVehicleNoticeCode, data)
