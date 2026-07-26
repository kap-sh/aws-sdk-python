"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentEffect``."""

from typing import Literal, TypeAlias, cast

RouteTransitIncidentEffect: TypeAlias = Literal[
    "Delayed",
    "Detoured",
    "Other",
    "ServiceAdded",
    "ServiceCancelled",
    "ServiceModified",
    "ServiceReduced",
    "StopMoved",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncidentEffect) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIncidentEffect:
    return cast(RouteTransitIncidentEffect, data)
