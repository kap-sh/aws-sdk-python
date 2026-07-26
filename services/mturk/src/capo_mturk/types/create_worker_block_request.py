"""Generated from Smithy shape ``com.amazonaws.mturk#CreateWorkerBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.string


class CreateWorkerBlockRequest(TypedDict, closed=True):
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker to block.</p>"""
    reason: "capo_mturk.types.string.String"
    """<p>A message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkerBlockRequest) -> dict:
    out: dict = {}
    out["WorkerId"] = value["worker_id"]
    out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkerBlockRequest:
    out: CreateWorkerBlockRequest = {}  # type: ignore[typeddict-item]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    else:
        raise DeserializationError("CreateWorkerBlockRequest.worker_id required")
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("CreateWorkerBlockRequest.reason required")
    return out
