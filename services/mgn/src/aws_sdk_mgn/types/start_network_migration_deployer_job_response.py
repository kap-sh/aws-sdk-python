"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationDeployerJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_job_id


class StartNetworkMigrationDeployerJobResponse(TypedDict):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the deployer job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationDeployerJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationDeployerJobResponse:
    out: StartNetworkMigrationDeployerJobResponse = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    return out
