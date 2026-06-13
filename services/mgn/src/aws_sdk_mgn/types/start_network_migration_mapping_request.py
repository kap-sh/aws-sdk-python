"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.security_group_mapping_strategy


class StartNetworkMigrationMappingRequest(TypedDict):
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    security_group_mapping_strategy: NotRequired[
        "aws_sdk_mgn.types.security_group_mapping_strategy.SecurityGroupMappingStrategy"
    ]
    """<p>The security group mapping strategy to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "security_group_mapping_strategy" in value:
        out["securityGroupMappingStrategy"] = value["security_group_mapping_strategy"]
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingRequest:
    out: StartNetworkMigrationMappingRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingRequest.network_migration_definition_id required"
        )
    if "securityGroupMappingStrategy" in data:
        out["security_group_mapping_strategy"] = data["securityGroupMappingStrategy"]
    return out
