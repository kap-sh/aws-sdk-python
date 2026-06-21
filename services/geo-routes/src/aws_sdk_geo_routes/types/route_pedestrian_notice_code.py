"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianNoticeCode``."""

from typing import Literal, TypeAlias, cast

RoutePedestrianNoticeCode: TypeAlias = Literal[
    "AccuratePolylineUnavailable",
    "Other",
    "ViolatedAvoidDirtRoad",
    "ViolatedAvoidTunnel",
    "ViolatedPedestrianOption",
    "ViolatedAvoidAreas",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianNoticeCode) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianNoticeCode:
    return cast(RoutePedestrianNoticeCode, data)
