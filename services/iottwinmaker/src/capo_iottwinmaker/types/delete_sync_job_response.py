"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteSyncJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.sync_job_state


class DeleteSyncJobResponse(TypedDict, closed=True):
    state: "capo_iottwinmaker.types.sync_job_state.SyncJobState"
    """<p>The SyncJob response state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSyncJobResponse) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> DeleteSyncJobResponse:
    out: DeleteSyncJobResponse = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("DeleteSyncJobResponse.state required")
    return out
