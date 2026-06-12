"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMulticastSourceUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multicast_source_update_request

__listOfMulticastSourceUpdateRequest: TypeAlias = list[
    "aws_sdk_medialive.types.multicast_source_update_request.MulticastSourceUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMulticastSourceUpdateRequest) -> list:
    import aws_sdk_medialive.types.multicast_source_update_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.multicast_source_update_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMulticastSourceUpdateRequest:
    import aws_sdk_medialive.types.multicast_source_update_request

    out: __listOfMulticastSourceUpdateRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.multicast_source_update_request.deserialize_json(
                item
            )
        )
    return out
