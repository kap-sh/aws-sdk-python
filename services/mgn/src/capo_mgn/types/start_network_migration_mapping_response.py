"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_job_id


class StartNetworkMigrationMappingResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_mgn.types.network_migration_job_id.NetworkMigrationJobID"]
    """<p>The unique identifier of the mapping job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingResponse:
    out: StartNetworkMigrationMappingResponse = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
