"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMulticastSourceCreateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.multicast_source_create_request

__listOfMulticastSourceCreateRequest: TypeAlias = list[
    "capo_medialive.types.multicast_source_create_request.MulticastSourceCreateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMulticastSourceCreateRequest) -> list:
    import capo_medialive.types.multicast_source_create_request

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.multicast_source_create_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMulticastSourceCreateRequest:
    import capo_medialive.types.multicast_source_create_request

    out: __listOfMulticastSourceCreateRequest = []
    for item in data:
        out.append(
            capo_medialive.types.multicast_source_create_request.deserialize_json(item)
        )
    return out
