"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMappingUpdatesFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter


class ListNetworkMigrationMappingUpdatesFilters(TypedDict):
    job_i_ds: NotRequired[
        "aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter.ListNetworkMigrationMappingUpdatesIDsFilter"
    ]
    """<p>A list of job IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMappingUpdatesFilters) -> dict:
    out: dict = {}
    if "job_i_ds" in value:
        import aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter

        out["jobIDs"] = (
            aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter.serialize_json(
                value["job_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMappingUpdatesFilters:
    out: ListNetworkMigrationMappingUpdatesFilters = {}  # type: ignore[typeddict-item]
    if "jobIDs" in data:
        import aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter

        out["job_i_ds"] = (
            aws_sdk_mgn.types.list_network_migration_mapping_updates_i_ds_filter.deserialize_json(
                data["jobIDs"]
            )
        )
    return out
