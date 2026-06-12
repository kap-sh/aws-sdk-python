"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentEffect``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Delayed",
        "Detoured",
        "Other",
        "ServiceAdded",
        "ServiceCancelled",
        "ServiceModified",
        "ServiceReduced",
        "StopMoved",
    )
)


def serialize_json(value: RouteTransitIncidentEffect) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIncidentEffect:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTransitIncidentEffect value: {data!r}"
        )
    return cast(RouteTransitIncidentEffect, data)
