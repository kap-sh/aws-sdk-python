"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationCodeGenerationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_job_id


class StartNetworkMigrationCodeGenerationResponse(TypedDict, closed=True):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the code generation job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationCodeGenerationResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationCodeGenerationResponse:
    out: StartNetworkMigrationCodeGenerationResponse = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
