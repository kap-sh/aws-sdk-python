"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

IsolineEngineType: TypeAlias = Literal[
    "Electric",
    "InternalCombustion",
    "PluginHybrid",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Electric",
        "InternalCombustion",
        "PluginHybrid",
    )
)


def serialize_json(value: IsolineEngineType) -> str:
    return value


def deserialize_json(data: str) -> IsolineEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsolineEngineType value: {data!r}")
    return cast(IsolineEngineType, data)
