"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaConnectFlowRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.media_connect_flow_request

__listOfMediaConnectFlowRequest: TypeAlias = list[
    "capo_medialive.types.media_connect_flow_request.MediaConnectFlowRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaConnectFlowRequest) -> list:
    import capo_medialive.types.media_connect_flow_request

    out: list = []
    for item in value:
        out.append(capo_medialive.types.media_connect_flow_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaConnectFlowRequest:
    import capo_medialive.types.media_connect_flow_request

    out: __listOfMediaConnectFlowRequest = []
    for item in data:
        out.append(
            capo_medialive.types.media_connect_flow_request.deserialize_json(item)
        )
    return out
