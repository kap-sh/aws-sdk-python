"""Generated from Smithy shape ``com.amazonaws.connect#DescribeQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.queue


class DescribeQueueResponse(TypedDict, closed=True):
    queue: NotRequired["capo_connect.types.queue.Queue"]
    """<p>The name of the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import capo_connect.types.queue

        out["Queue"] = capo_connect.types.queue.serialize_json(value["queue"])
    return out


def deserialize_json(data: dict) -> DescribeQueueResponse:
    out: DescribeQueueResponse = {}  # type: ignore[typeddict-item]
    if "Queue" in data:
        import capo_connect.types.queue

        out["queue"] = capo_connect.types.queue.deserialize_json(data["Queue"])
    return out
