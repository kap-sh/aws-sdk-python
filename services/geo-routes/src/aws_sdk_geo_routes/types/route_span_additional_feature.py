"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteSpanAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanAdditionalFeature:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteSpanAdditionalFeature value: {data!r}"
        )
    return cast(RouteSpanAdditionalFeature, data)
