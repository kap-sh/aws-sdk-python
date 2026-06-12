"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaConnectFlow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_connect_flow

__listOfMediaConnectFlow: TypeAlias = list[
    "aws_sdk_medialive.types.media_connect_flow.MediaConnectFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaConnectFlow) -> list:
    import aws_sdk_medialive.types.media_connect_flow

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.media_connect_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaConnectFlow:
    import aws_sdk_medialive.types.media_connect_flow

    out: __listOfMediaConnectFlow = []
    for item in data:
        out.append(aws_sdk_medialive.types.media_connect_flow.deserialize_json(item))
    return out
