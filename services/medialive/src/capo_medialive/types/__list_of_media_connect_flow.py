"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaConnectFlow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.media_connect_flow

__listOfMediaConnectFlow: TypeAlias = list[
    "capo_medialive.types.media_connect_flow.MediaConnectFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaConnectFlow) -> list:
    import capo_medialive.types.media_connect_flow

    out: list = []
    for item in value:
        out.append(capo_medialive.types.media_connect_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaConnectFlow:
    import capo_medialive.types.media_connect_flow

    out: __listOfMediaConnectFlow = []
    for item in data:
        out.append(capo_medialive.types.media_connect_flow.deserialize_json(item))
    return out
