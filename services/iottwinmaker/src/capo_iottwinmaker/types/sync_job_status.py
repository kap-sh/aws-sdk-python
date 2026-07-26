"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncJobStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_details
    import capo_iottwinmaker.types.sync_job_state


class SyncJobStatus(TypedDict, closed=True):
    state: NotRequired["capo_iottwinmaker.types.sync_job_state.SyncJobState"]
    """<p>The SyncJob status state.</p>"""
    error: NotRequired["capo_iottwinmaker.types.error_details.ErrorDetails"]
    """<p>The SyncJob error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncJobStatus) -> dict:
    out: dict = {}
    if "state" in value:
        out["state"] = value["state"]
    if "error" in value:
        import capo_iottwinmaker.types.error_details

        out["error"] = capo_iottwinmaker.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> SyncJobStatus:
    out: SyncJobStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    if "error" in data:
        import capo_iottwinmaker.types.error_details

        out["error"] = capo_iottwinmaker.types.error_details.deserialize_json(
            data["error"]
        )
    return out
