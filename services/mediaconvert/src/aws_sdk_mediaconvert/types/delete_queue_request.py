"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DeleteQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class DeleteQueueRequest(TypedDict, closed=True):
    name: "aws_sdk_mediaconvert.types.__string.__string"
    """The name of the queue that you want to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteQueueRequest:
    out: DeleteQueueRequest = {}  # type: ignore[typeddict-item]
    return out
