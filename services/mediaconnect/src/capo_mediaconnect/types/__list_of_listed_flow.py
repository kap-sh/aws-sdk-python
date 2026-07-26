"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedFlow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.listed_flow

__listOfListedFlow: TypeAlias = list["capo_mediaconnect.types.listed_flow.ListedFlow"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedFlow) -> list:
    import capo_mediaconnect.types.listed_flow

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.listed_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListedFlow:
    import capo_mediaconnect.types.listed_flow

    out: __listOfListedFlow = []
    for item in data:
        out.append(capo_mediaconnect.types.listed_flow.deserialize_json(item))
    return out
