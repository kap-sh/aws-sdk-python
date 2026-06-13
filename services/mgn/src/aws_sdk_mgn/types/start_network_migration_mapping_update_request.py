"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.start_network_migration_mapping_update_constructs
    import aws_sdk_mgn.types.start_network_migration_mapping_update_segments


class StartNetworkMigrationMappingUpdateRequest(TypedDict):
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    constructs: NotRequired[
        "aws_sdk_mgn.types.start_network_migration_mapping_update_constructs.StartNetworkMigrationMappingUpdateConstructs"
    ]
    """<p>A list of construct updates to apply.</p>"""
    segments: NotRequired[
        "aws_sdk_mgn.types.start_network_migration_mapping_update_segments.StartNetworkMigrationMappingUpdateSegments"
    ]
    """<p>A list of segment updates to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "constructs" in value:
        import aws_sdk_mgn.types.start_network_migration_mapping_update_constructs

        out["constructs"] = (
            aws_sdk_mgn.types.start_network_migration_mapping_update_constructs.serialize_json(
                value["constructs"]
            )
        )
    if "segments" in value:
        import aws_sdk_mgn.types.start_network_migration_mapping_update_segments

        out["segments"] = (
            aws_sdk_mgn.types.start_network_migration_mapping_update_segments.serialize_json(
                value["segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateRequest:
    out: StartNetworkMigrationMappingUpdateRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateRequest.network_migration_execution_id required"
        )
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateRequest.network_migration_definition_id required"
        )
    if "constructs" in data:
        import aws_sdk_mgn.types.start_network_migration_mapping_update_constructs

        out["constructs"] = (
            aws_sdk_mgn.types.start_network_migration_mapping_update_constructs.deserialize_json(
                data["constructs"]
            )
        )
    if "segments" in data:
        import aws_sdk_mgn.types.start_network_migration_mapping_update_segments

        out["segments"] = (
            aws_sdk_mgn.types.start_network_migration_mapping_update_segments.deserialize_json(
                data["segments"]
            )
        )
    return out
