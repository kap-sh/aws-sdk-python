"""Generated from Smithy shape ``com.amazonaws.outposts#ShipmentCarrier``."""

from typing import Literal, TypeAlias, cast

ShipmentCarrier: TypeAlias = Literal[
    "DHL",
    "DBS",
    "FEDEX",
    "UPS",
    "EXPEDITORS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShipmentCarrier) -> str:
    return value


def deserialize_json(data: str) -> ShipmentCarrier:
    return cast(ShipmentCarrier, data)
