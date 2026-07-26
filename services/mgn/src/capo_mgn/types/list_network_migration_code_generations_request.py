"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationCodeGenerationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_code_generations_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.pagination_token


class ListNetworkMigrationCodeGenerationsRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    filters: NotRequired[
        "capo_mgn.types.list_network_migration_code_generations_filters.ListNetworkMigrationCodeGenerationsFilters"
    ]
    """<p>Filters to apply when listing code generation jobs.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationCodeGenerationsRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "filters" in value:
        import capo_mgn.types.list_network_migration_code_generations_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_code_generations_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationCodeGenerationsRequest:
    out: ListNetworkMigrationCodeGenerationsRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "ListNetworkMigrationCodeGenerationsRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "ListNetworkMigrationCodeGenerationsRequest.network_migration_definition_id required"
        )
    if "filters" in data:
        import capo_mgn.types.list_network_migration_code_generations_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_code_generations_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
