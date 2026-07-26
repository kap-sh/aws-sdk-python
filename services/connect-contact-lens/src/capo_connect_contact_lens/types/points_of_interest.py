"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#PointsOfInterest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect_contact_lens.types.point_of_interest

PointsOfInterest: TypeAlias = list[
    "capo_connect_contact_lens.types.point_of_interest.PointOfInterest"
]


# --- restJson1 ser/de ---
def serialize_json(value: PointsOfInterest) -> list:
    import capo_connect_contact_lens.types.point_of_interest

    out: list = []
    for item in value:
        out.append(
            capo_connect_contact_lens.types.point_of_interest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PointsOfInterest:
    import capo_connect_contact_lens.types.point_of_interest

    out: PointsOfInterest = []
    for item in data:
        out.append(
            capo_connect_contact_lens.types.point_of_interest.deserialize_json(item)
        )
    return out
