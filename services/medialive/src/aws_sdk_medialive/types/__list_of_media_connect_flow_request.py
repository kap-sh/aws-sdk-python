"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaConnectFlowRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_connect_flow_request

__listOfMediaConnectFlowRequest: TypeAlias = list[
    "aws_sdk_medialive.types.media_connect_flow_request.MediaConnectFlowRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaConnectFlowRequest) -> list:
    import aws_sdk_medialive.types.media_connect_flow_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.media_connect_flow_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMediaConnectFlowRequest:
    import aws_sdk_medialive.types.media_connect_flow_request

    out: __listOfMediaConnectFlowRequest = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.media_connect_flow_request.deserialize_json(item)
        )
    return out
