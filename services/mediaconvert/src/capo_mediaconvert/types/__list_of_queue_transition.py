"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfQueueTransition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.queue_transition

__listOfQueueTransition: TypeAlias = list[
    "capo_mediaconvert.types.queue_transition.QueueTransition"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfQueueTransition) -> list:
    import capo_mediaconvert.types.queue_transition

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.queue_transition.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfQueueTransition:
    import capo_mediaconvert.types.queue_transition

    out: __listOfQueueTransition = []
    for item in data:
        out.append(capo_mediaconvert.types.queue_transition.deserialize_json(item))
    return out
