"""Generated from Smithy shape ``com.amazonaws.outposts#PowerConnector``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

PowerConnector: TypeAlias = Literal[
    "L6_30P",
    "IEC309",
    "AH530P7W",
    "AH532P6W",
    "CS8365C",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "L6_30P",
        "IEC309",
        "AH530P7W",
        "AH532P6W",
        "CS8365C",
    )
)


def serialize_json(value: PowerConnector) -> str:
    return value


def deserialize_json(data: str) -> PowerConnector:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PowerConnector value: {data!r}")
    return cast(PowerConnector, data)
