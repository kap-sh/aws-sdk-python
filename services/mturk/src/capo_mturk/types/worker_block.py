"""Generated from Smithy shape ``com.amazonaws.mturk#WorkerBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.string


class WorkerBlock(TypedDict, closed=True):
    worker_id: NotRequired["capo_mturk.types.customer_id.CustomerId"]
    """<p> The ID of the Worker who accepted the HIT.</p>"""
    reason: NotRequired["capo_mturk.types.string.String"]
    """<p> A message explaining the reason the Worker was blocked. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkerBlock) -> dict:
    out: dict = {}
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkerBlock:
    out: WorkerBlock = {}  # type: ignore[typeddict-item]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
