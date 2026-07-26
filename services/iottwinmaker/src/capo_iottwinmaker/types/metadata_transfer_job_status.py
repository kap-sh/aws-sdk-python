"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#MetadataTransferJobStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_details
    import capo_iottwinmaker.types.integer
    import capo_iottwinmaker.types.metadata_transfer_job_state


class MetadataTransferJobStatus(TypedDict, closed=True):
    state: NotRequired[
        "capo_iottwinmaker.types.metadata_transfer_job_state.MetadataTransferJobState"
    ]
    """<p>The metadata transfer job state.</p>"""
    error: NotRequired["capo_iottwinmaker.types.error_details.ErrorDetails"]
    """<p>The metadata transfer job error.</p>"""
    queued_position: NotRequired["capo_iottwinmaker.types.integer.Integer"]
    """<p>The queued position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataTransferJobStatus) -> dict:
    out: dict = {}
    if "state" in value:
        out["state"] = value["state"]
    if "error" in value:
        import capo_iottwinmaker.types.error_details

        out["error"] = capo_iottwinmaker.types.error_details.serialize_json(
            value["error"]
        )
    if "queued_position" in value:
        out["queuedPosition"] = value["queued_position"]
    return out


def deserialize_json(data: dict) -> MetadataTransferJobStatus:
    out: MetadataTransferJobStatus = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    if "error" in data:
        import capo_iottwinmaker.types.error_details

        out["error"] = capo_iottwinmaker.types.error_details.deserialize_json(
            data["error"]
        )
    if "queuedPosition" in data:
        out["queued_position"] = data["queuedPosition"]
    return out
