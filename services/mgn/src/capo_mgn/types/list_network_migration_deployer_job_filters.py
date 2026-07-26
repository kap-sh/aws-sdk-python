"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDeployerJobFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_deployer_job_i_ds_filters


class ListNetworkMigrationDeployerJobFilters(TypedDict, closed=True):
    job_i_ds: NotRequired[
        "capo_mgn.types.list_network_migration_deployer_job_i_ds_filters.ListNetworkMigrationDeployerJobIDsFilters"
    ]
    """<p>A list of job IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDeployerJobFilters) -> dict:
    out: dict = {}
    if "job_i_ds" in value:
        import capo_mgn.types.list_network_migration_deployer_job_i_ds_filters

        out["jobIDs"] = (
            capo_mgn.types.list_network_migration_deployer_job_i_ds_filters.serialize_json(
                value["job_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDeployerJobFilters:
    out: ListNetworkMigrationDeployerJobFilters = {}  # type: ignore[typeddict-item]
    if "jobIDs" in data:
        import capo_mgn.types.list_network_migration_deployer_job_i_ds_filters

        out["job_i_ds"] = (
            capo_mgn.types.list_network_migration_deployer_job_i_ds_filters.deserialize_json(
                data["jobIDs"]
            )
        )
    return out
