"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateNetworkMigrationDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_description
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.source_configuration_list
    import capo_mgn.types.target_deployment
    import capo_mgn.types.target_network_update
    import capo_mgn.types.target_s3_configuration_update


class UpdateNetworkMigrationDefinitionRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition to update.</p>"""
    name: NotRequired[
        "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The updated name of the network migration definition.</p>"""
    description: NotRequired[
        "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
    ]
    """<p>The updated description of the network migration definition.</p>"""
    source_configurations: NotRequired[
        "capo_mgn.types.source_configuration_list.SourceConfigurationList"
    ]
    """<p>The updated list of source configurations.</p>"""
    target_s3_configuration: NotRequired[
        "capo_mgn.types.target_s3_configuration_update.TargetS3ConfigurationUpdate"
    ]
    """<p>The updated S3 configuration for storing the target network artifacts.</p>"""
    target_network: NotRequired[
        "capo_mgn.types.target_network_update.TargetNetworkUpdate"
    ]
    """<p>The updated target network configuration.</p>"""
    target_deployment: NotRequired["capo_mgn.types.target_deployment.TargetDeployment"]
    """<p>The updated target deployment configuration.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkMigrationDefinitionRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "source_configurations" in value:
        import capo_mgn.types.source_configuration_list

        out["sourceConfigurations"] = (
            capo_mgn.types.source_configuration_list.serialize_json(
                value["source_configurations"]
            )
        )
    if "target_s3_configuration" in value:
        import capo_mgn.types.target_s3_configuration_update

        out["targetS3Configuration"] = (
            capo_mgn.types.target_s3_configuration_update.serialize_json(
                value["target_s3_configuration"]
            )
        )
    if "target_network" in value:
        import capo_mgn.types.target_network_update

        out["targetNetwork"] = capo_mgn.types.target_network_update.serialize_json(
            value["target_network"]
        )
    if "target_deployment" in value:
        out["targetDeployment"] = value["target_deployment"]
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkMigrationDefinitionRequest:
    out: UpdateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "UpdateNetworkMigrationDefinitionRequest.network_migration_definition_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sourceConfigurations" in data:
        import capo_mgn.types.source_configuration_list

        out["source_configurations"] = (
            capo_mgn.types.source_configuration_list.deserialize_json(
                data["sourceConfigurations"]
            )
        )
    if "targetS3Configuration" in data:
        import capo_mgn.types.target_s3_configuration_update

        out["target_s3_configuration"] = (
            capo_mgn.types.target_s3_configuration_update.deserialize_json(
                data["targetS3Configuration"]
            )
        )
    if "targetNetwork" in data:
        import capo_mgn.types.target_network_update

        out["target_network"] = capo_mgn.types.target_network_update.deserialize_json(
            data["targetNetwork"]
        )
    if "targetDeployment" in data:
        out["target_deployment"] = data["targetDeployment"]
    if "scopeTags" in data:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
