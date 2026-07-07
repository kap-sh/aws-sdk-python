"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationExecutionRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_execution_i_ds_filter
    import aws_sdk_mgn.types.network_migration_execution_statuses_filter


class ListNetworkMigrationExecutionRequestFilters(TypedDict, closed=True):
    network_migration_execution_i_ds: NotRequired[
        "aws_sdk_mgn.types.network_migration_execution_i_ds_filter.NetworkMigrationExecutionIDsFilter"
    ]
    """<p>A list of execution IDs to filter by.</p>"""
    network_migration_execution_statuses: NotRequired[
        "aws_sdk_mgn.types.network_migration_execution_statuses_filter.NetworkMigrationExecutionStatusesFilter"
    ]
    """<p>A list of execution statuses to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationExecutionRequestFilters) -> dict:
    out: dict = {}
    if "network_migration_execution_i_ds" in value:
        import aws_sdk_mgn.types.network_migration_execution_i_ds_filter

        out["networkMigrationExecutionIDs"] = (
            aws_sdk_mgn.types.network_migration_execution_i_ds_filter.serialize_json(
                value["network_migration_execution_i_ds"]
            )
        )
    if "network_migration_execution_statuses" in value:
        import aws_sdk_mgn.types.network_migration_execution_statuses_filter

        out["networkMigrationExecutionStatuses"] = (
            aws_sdk_mgn.types.network_migration_execution_statuses_filter.serialize_json(
                value["network_migration_execution_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationExecutionRequestFilters:
    out: ListNetworkMigrationExecutionRequestFilters = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionIDs" in data:
        import aws_sdk_mgn.types.network_migration_execution_i_ds_filter

        out["network_migration_execution_i_ds"] = (
            aws_sdk_mgn.types.network_migration_execution_i_ds_filter.deserialize_json(
                data["networkMigrationExecutionIDs"]
            )
        )
    if "networkMigrationExecutionStatuses" in data:
        import aws_sdk_mgn.types.network_migration_execution_statuses_filter

        out["network_migration_execution_statuses"] = (
            aws_sdk_mgn.types.network_migration_execution_statuses_filter.deserialize_json(
                data["networkMigrationExecutionStatuses"]
            )
        )
    return out
