"""Generated from Smithy shape ``com.amazonaws.connect#DescribeQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.queue


class DescribeQueueResponse(TypedDict):
    queue: NotRequired["aws_sdk_connect.types.queue.Queue"]
    """<p>The name of the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import aws_sdk_connect.types.queue

        out["Queue"] = aws_sdk_connect.types.queue.serialize_json(value["queue"])
    return out


def deserialize_json(data: dict) -> DescribeQueueResponse:
    out: DescribeQueueResponse = {}  # type: ignore[typeddict-item]
    if "Queue" in data:
        import aws_sdk_connect.types.queue

        out["queue"] = aws_sdk_connect.types.queue.deserialize_json(data["Queue"])
    return out
