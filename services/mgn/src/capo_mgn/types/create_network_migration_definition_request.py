"""Generated from Smithy shape ``com.amazonaws.mgn#CreateNetworkMigrationDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_description
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.source_configuration_list
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_deployment
    import capo_mgn.types.target_network
    import capo_mgn.types.target_s3_configuration


class CreateNetworkMigrationDefinitionRequest(TypedDict, closed=True):
    name: "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    """<p>The name of the network migration definition.</p>"""
    description: NotRequired[
        "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
    ]
    """<p>A description of the network migration definition.</p>"""
    source_configurations: NotRequired[
        "capo_mgn.types.source_configuration_list.SourceConfigurationList"
    ]
    """<p>A list of source configurations for the network migration.</p>"""
    target_s3_configuration: (
        "capo_mgn.types.target_s3_configuration.TargetS3Configuration"
    )
    """<p>The S3 configuration for storing the target network artifacts.</p>"""
    target_network: "capo_mgn.types.target_network.TargetNetwork"
    """<p>The target network configuration including topology and CIDR ranges.</p>"""
    target_deployment: NotRequired["capo_mgn.types.target_deployment.TargetDeployment"]
    """<p>The target deployment configuration for the migrated network.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Tags to assign to the network migration definition.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the network migration definition to control access and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkMigrationDefinitionRequest) -> dict:
    out: dict = {}
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
    import capo_mgn.types.target_s3_configuration

    out["targetS3Configuration"] = (
        capo_mgn.types.target_s3_configuration.serialize_json(
            value["target_s3_configuration"]
        )
    )
    import capo_mgn.types.target_network

    out["targetNetwork"] = capo_mgn.types.target_network.serialize_json(
        value["target_network"]
    )
    if "target_deployment" in value:
        out["targetDeployment"] = value["target_deployment"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNetworkMigrationDefinitionRequest:
    out: CreateNetworkMigrationDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateNetworkMigrationDefinitionRequest.name required"
        )
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
        import capo_mgn.types.target_s3_configuration

        out["target_s3_configuration"] = (
            capo_mgn.types.target_s3_configuration.deserialize_json(
                data["targetS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNetworkMigrationDefinitionRequest.target_s3_configuration required"
        )
    if "targetNetwork" in data:
        import capo_mgn.types.target_network

        out["target_network"] = capo_mgn.types.target_network.deserialize_json(
            data["targetNetwork"]
        )
    else:
        raise DeserializationError(
            "CreateNetworkMigrationDefinitionRequest.target_network required"
        )
    if "targetDeployment" in data:
        out["target_deployment"] = data["targetDeployment"]
    if "tags" in data:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if "scopeTags" in data:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
