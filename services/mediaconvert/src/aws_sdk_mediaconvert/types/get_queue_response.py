"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.queue


class GetQueueResponse(TypedDict):
    queue: NotRequired["aws_sdk_mediaconvert.types.queue.Queue"]
    """You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html."""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import aws_sdk_mediaconvert.types.queue

        out["queue"] = aws_sdk_mediaconvert.types.queue.serialize_json(value["queue"])
    return out


def deserialize_json(data: dict) -> GetQueueResponse:
    out: GetQueueResponse = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        import aws_sdk_mediaconvert.types.queue

        out["queue"] = aws_sdk_mediaconvert.types.queue.deserialize_json(data["queue"])
    return out
