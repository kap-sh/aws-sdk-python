"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfOffering``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.offering

__listOfOffering: TypeAlias = list["capo_medialive.types.offering.Offering"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOffering) -> list:
    import capo_medialive.types.offering

    out: list = []
    for item in value:
        out.append(capo_medialive.types.offering.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOffering:
    import capo_medialive.types.offering

    out: __listOfOffering = []
    for item in data:
        out.append(capo_medialive.types.offering.deserialize_json(item))
    return out
