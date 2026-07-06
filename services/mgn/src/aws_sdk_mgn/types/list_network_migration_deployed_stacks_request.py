"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDeployedStacksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.pagination_token


class ListNetworkMigrationDeployedStacksRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDeployedStacksRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationDeployedStacksRequest:
    out: ListNetworkMigrationDeployedStacksRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "ListNetworkMigrationDeployedStacksRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "ListNetworkMigrationDeployedStacksRequest.network_migration_definition_id required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
