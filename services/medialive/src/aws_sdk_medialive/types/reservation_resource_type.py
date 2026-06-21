"""Generated from Smithy shape ``com.amazonaws.medialive#ReservationResourceType``."""

from typing import Literal, TypeAlias, cast

"""Resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'"""
ReservationResourceType: TypeAlias = Literal[
    "INPUT",
    "OUTPUT",
    "MULTIPLEX",
    "CHANNEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationResourceType) -> str:
    return value


def deserialize_json(data: str) -> ReservationResourceType:
    return cast(ReservationResourceType, data)
