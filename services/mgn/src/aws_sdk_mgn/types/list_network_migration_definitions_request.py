"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_network_migration_definitions_request_filters
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class ListNetworkMigrationDefinitionsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_mgn.types.list_network_migration_definitions_request_filters.ListNetworkMigrationDefinitionsRequestFilters"
    ]
    """<p>Filters to apply when listing network migration definitions.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDefinitionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mgn.types.list_network_migration_definitions_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.list_network_migration_definitions_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDefinitionsRequest:
    out: ListNetworkMigrationDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mgn.types.list_network_migration_definitions_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.list_network_migration_definitions_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
