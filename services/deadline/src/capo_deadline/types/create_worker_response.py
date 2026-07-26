"""Generated from Smithy shape ``com.amazonaws.deadline#CreateWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.worker_id


class CreateWorkerResponse(TypedDict, closed=True):
    worker_id: "capo_deadline.types.worker_id.WorkerId"
    """<p>The worker ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerResponse) -> dict:
    out: dict = {}
    out["workerId"] = value["worker_id"]
    return out


def deserialize_json(data: dict) -> CreateWorkerResponse:
    out: CreateWorkerResponse = {}  # type: ignore[typeddict-item]
    if "workerId" in data:
        out["worker_id"] = data["workerId"]
    else:
        raise DeserializationError("CreateWorkerResponse.worker_id required")
    return out
