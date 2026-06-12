"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineZoneCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

IsolineZoneCategory: TypeAlias = Literal[
    "CongestionPricing",
    "Environmental",
    "Vignette",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CongestionPricing",
        "Environmental",
        "Vignette",
    )
)


def serialize_json(value: IsolineZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> IsolineZoneCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsolineZoneCategory value: {data!r}")
    return cast(IsolineZoneCategory, data)
