"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_job_id


class StartNetworkMigrationAnalysisResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_mgn.types.network_migration_job_id.NetworkMigrationJobID"]
    """<p>The unique identifier of the analysis job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationAnalysisResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationAnalysisResponse:
    out: StartNetworkMigrationAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
