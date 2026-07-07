"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.network_migration_definition_description
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_definition_name
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.source_configuration_list
    import aws_sdk_mgn.types.tags_map
    import aws_sdk_mgn.types.target_deployment
    import aws_sdk_mgn.types.target_network
    import aws_sdk_mgn.types.target_s3_configuration


class NetworkMigrationDefinition(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the network migration definition.</p>"""
    network_migration_definition_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    name: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The name of the network migration definition.</p>"""
    description: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
    ]
    """<p>A description of the network migration definition.</p>"""
    source_configurations: NotRequired[
        "aws_sdk_mgn.types.source_configuration_list.SourceConfigurationList"
    ]
    """<p>A list of source configurations for the network migration.</p>"""
    target_s3_configuration: NotRequired[
        "aws_sdk_mgn.types.target_s3_configuration.TargetS3Configuration"
    ]
    """<p>The S3 configuration for storing the target network artifacts.</p>"""
    target_network: NotRequired["aws_sdk_mgn.types.target_network.TargetNetwork"]
    """<p>The target network configuration including topology and CIDR ranges.</p>"""
    target_deployment: NotRequired[
        "aws_sdk_mgn.types.target_deployment.TargetDeployment"
    ]
    """<p>The target deployment configuration for the migrated network.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the network migration definition was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the network migration definition was last updated.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the network migration definition.</p>"""
    scope_tags: NotRequired["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinition) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "source_configurations" in value:
        import aws_sdk_mgn.types.source_configuration_list

        out["sourceConfigurations"] = (
            aws_sdk_mgn.types.source_configuration_list.serialize_json(
                value["source_configurations"]
            )
        )
    if "target_s3_configuration" in value:
        import aws_sdk_mgn.types.target_s3_configuration

        out["targetS3Configuration"] = (
            aws_sdk_mgn.types.target_s3_configuration.serialize_json(
                value["target_s3_configuration"]
            )
        )
    if "target_network" in value:
        import aws_sdk_mgn.types.target_network

        out["targetNetwork"] = aws_sdk_mgn.types.target_network.serialize_json(
            value["target_network"]
        )
    if "target_deployment" in value:
        out["targetDeployment"] = value["target_deployment"]
    if "created_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["createdAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "scope_tags" in value:
        import aws_sdk_mgn.types.scope_tags_map

        out["scopeTags"] = aws_sdk_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationDefinition:
    out: NetworkMigrationDefinition = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "sourceConfigurations" in data:
        import aws_sdk_mgn.types.source_configuration_list

        out["source_configurations"] = (
            aws_sdk_mgn.types.source_configuration_list.deserialize_json(
                data["sourceConfigurations"]
            )
        )
    if "targetS3Configuration" in data:
        import aws_sdk_mgn.types.target_s3_configuration

        out["target_s3_configuration"] = (
            aws_sdk_mgn.types.target_s3_configuration.deserialize_json(
                data["targetS3Configuration"]
            )
        )
    if "targetNetwork" in data:
        import aws_sdk_mgn.types.target_network

        out["target_network"] = aws_sdk_mgn.types.target_network.deserialize_json(
            data["targetNetwork"]
        )
    if "targetDeployment" in data:
        out["target_deployment"] = data["targetDeployment"]
    if "createdAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["created_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["updated_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "scopeTags" in data:
        import aws_sdk_mgn.types.scope_tags_map

        out["scope_tags"] = aws_sdk_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
