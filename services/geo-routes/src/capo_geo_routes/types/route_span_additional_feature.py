"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

RouteSpanAdditionalFeature: TypeAlias = Literal[
    "BestCaseDuration",
    "CarAccess",
    "Country",
    "Distance",
    "Duration",
    "DynamicSpeed",
    "FunctionalClassification",
    "Gates",
    "Incidents",
    "Names",
    "Notices",
    "PedestrianAccess",
    "RailwayCrossings",
    "Region",
    "RoadAttributes",
    "RouteNumbers",
    "ScooterAccess",
    "SpeedLimit",
    "TollSystems",
    "TruckAccess",
    "TruckRoadTypes",
    "TypicalDuration",
    "Zones",
    "Consumption",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanAdditionalFeature:
    return cast(RouteSpanAdditionalFeature, data)
