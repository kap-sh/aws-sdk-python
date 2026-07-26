"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMappingsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_mappings_i_ds_filter


class ListNetworkMigrationMappingsFilters(TypedDict, closed=True):
    job_i_ds: NotRequired[
        "capo_mgn.types.list_network_migration_mappings_i_ds_filter.ListNetworkMigrationMappingsIDsFilter"
    ]
    """<p>A list of job IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMappingsFilters) -> dict:
    out: dict = {}
    if "job_i_ds" in value:
        import capo_mgn.types.list_network_migration_mappings_i_ds_filter

        out["jobIDs"] = (
            capo_mgn.types.list_network_migration_mappings_i_ds_filter.serialize_json(
                value["job_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMappingsFilters:
    out: ListNetworkMigrationMappingsFilters = {}  # type: ignore[typeddict-item]
    if "jobIDs" in data:
        import capo_mgn.types.list_network_migration_mappings_i_ds_filter

        out["job_i_ds"] = (
            capo_mgn.types.list_network_migration_mappings_i_ds_filter.deserialize_json(
                data["jobIDs"]
            )
        )
    return out
