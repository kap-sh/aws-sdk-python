"""Generated from Smithy shape ``com.amazonaws.mgn#GetNetworkMigrationDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_mgn.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_definition_id

class GetNetworkMigrationDefinitionRequest(TypedDict):
    network_migration_definition_id: "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    """<p>The unique identifier of the network migration definition to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkMigrationDefinitionRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    return out


def deserialize_json(data: dict) -> GetNetworkMigrationDefinitionRequest:
    out: GetNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError("GetNetworkMigrationDefinitionRequest.network_migration_definition_id required")
    return out