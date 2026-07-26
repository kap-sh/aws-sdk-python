"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAddOutputRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_output_request

__listOfAddOutputRequest: TypeAlias = list[
    "capo_mediaconnect.types.add_output_request.AddOutputRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAddOutputRequest) -> list:
    import capo_mediaconnect.types.add_output_request

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.add_output_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAddOutputRequest:
    import capo_mediaconnect.types.add_output_request

    out: __listOfAddOutputRequest = []
    for item in data:
        out.append(capo_mediaconnect.types.add_output_request.deserialize_json(item))
    return out
