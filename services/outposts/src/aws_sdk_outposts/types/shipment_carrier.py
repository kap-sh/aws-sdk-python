"""Generated from Smithy shape ``com.amazonaws.outposts#ShipmentCarrier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

ShipmentCarrier: TypeAlias = Literal[
    "DHL",
    "DBS",
    "FEDEX",
    "UPS",
    "EXPEDITORS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DHL",
        "DBS",
        "FEDEX",
        "UPS",
        "EXPEDITORS",
    )
)


def serialize_json(value: ShipmentCarrier) -> str:
    return value


def deserialize_json(data: str) -> ShipmentCarrier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShipmentCarrier value: {data!r}")
    return cast(ShipmentCarrier, data)
