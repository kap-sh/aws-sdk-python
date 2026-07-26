"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.queue


class UpdateQueueResponse(TypedDict, closed=True):
    queue: NotRequired["capo_pcs.types.queue.Queue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import capo_pcs.types.queue

        out["queue"] = capo_pcs.types.queue.serialize_aws_json_1_0(value["queue"])
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateQueueResponse:
    out: UpdateQueueResponse = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        import capo_pcs.types.queue

        out["queue"] = capo_pcs.types.queue.deserialize_aws_json_1_0(data["queue"])
    return out
