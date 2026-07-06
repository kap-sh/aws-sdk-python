"""Generated from Smithy shape ``com.amazonaws.pcs#CreateQueueResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.queue


class CreateQueueResponse(TypedDict, closed=True):
    queue: NotRequired["aws_sdk_pcs.types.queue.Queue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import aws_sdk_pcs.types.queue

        out["queue"] = aws_sdk_pcs.types.queue.serialize_aws_json_1_0(value["queue"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateQueueResponse:
    out: CreateQueueResponse = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        import aws_sdk_pcs.types.queue

        out["queue"] = aws_sdk_pcs.types.queue.deserialize_aws_json_1_0(data["queue"])
    return out
