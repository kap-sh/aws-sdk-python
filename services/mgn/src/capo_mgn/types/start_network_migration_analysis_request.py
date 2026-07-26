"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id


class StartNetworkMigrationAnalysisRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution to analyze.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationAnalysisRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationAnalysisRequest:
    out: StartNetworkMigrationAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationAnalysisRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationAnalysisRequest.network_migration_definition_id required"
        )
    return out
