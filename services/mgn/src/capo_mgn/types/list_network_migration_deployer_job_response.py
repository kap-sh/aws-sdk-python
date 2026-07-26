"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDeployerJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_deployer_job_list
    import capo_mgn.types.pagination_token


class ListNetworkMigrationDeployerJobResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.network_migration_deployer_job_list.NetworkMigrationDeployerJobList"
    ]
    """<p>A list of deployer job details.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDeployerJobResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.network_migration_deployer_job_list

        out["items"] = (
            capo_mgn.types.network_migration_deployer_job_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDeployerJobResponse:
    out: ListNetworkMigrationDeployerJobResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.network_migration_deployer_job_list

        out["items"] = (
            capo_mgn.types.network_migration_deployer_job_list.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
