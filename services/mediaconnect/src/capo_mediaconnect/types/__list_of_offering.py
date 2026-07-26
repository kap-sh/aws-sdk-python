"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfOffering``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.offering

__listOfOffering: TypeAlias = list["capo_mediaconnect.types.offering.Offering"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOffering) -> list:
    import capo_mediaconnect.types.offering

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.offering.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOffering:
    import capo_mediaconnect.types.offering

    out: __listOfOffering = []
    for item in data:
        out.append(capo_mediaconnect.types.offering.deserialize_json(item))
    return out
