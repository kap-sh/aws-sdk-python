"""Generated from Smithy shape ``com.amazonaws.pcs#GetQueueResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.queue


class GetQueueResponse(TypedDict):
    queue: NotRequired["aws_sdk_pcs.types.queue.Queue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueResponse) -> dict:
    out: dict = {}
    if "queue" in value:
        import aws_sdk_pcs.types.queue

        out["queue"] = aws_sdk_pcs.types.queue.serialize_aws_json_1_0(value["queue"])
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueResponse:
    out: GetQueueResponse = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        import aws_sdk_pcs.types.queue

        out["queue"] = aws_sdk_pcs.types.queue.deserialize_aws_json_1_0(data["queue"])
    return out
