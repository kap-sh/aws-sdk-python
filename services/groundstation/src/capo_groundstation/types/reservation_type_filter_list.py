"""Generated from Smithy shape ``com.amazonaws.groundstation#ReservationTypeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.reservation_type

ReservationTypeFilterList: TypeAlias = list[
    "capo_groundstation.types.reservation_type.ReservationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReservationTypeFilterList) -> list:
    import capo_groundstation.types.reservation_type

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.reservation_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReservationTypeFilterList:
    import capo_groundstation.types.reservation_type

    out: ReservationTypeFilterList = []
    for item in data:
        out.append(capo_groundstation.types.reservation_type.deserialize_json(item))
    return out
