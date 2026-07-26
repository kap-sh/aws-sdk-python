"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.endpoint

__listOfEndpoint: TypeAlias = list["capo_mediaconvert.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEndpoint) -> list:
    import capo_mediaconvert.types.endpoint

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfEndpoint:
    import capo_mediaconvert.types.endpoint

    out: __listOfEndpoint = []
    for item in data:
        out.append(capo_mediaconvert.types.endpoint.deserialize_json(item))
    return out
