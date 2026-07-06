"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_definition_name
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.source_environment
    import aws_sdk_mgn.types.tags_map


class NetworkMigrationDefinitionSummary(TypedDict, closed=True):
    network_migration_definition_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    name: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
    ]
    """<p>The name of the network migration definition.</p>"""
    source_environment: NotRequired[
        "aws_sdk_mgn.types.source_environment.SourceEnvironment"
    ]
    """<p>The source environment configuration.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the network migration definition.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Tags assigned to the network migration definition.</p>"""
    scope_tags: NotRequired["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the network migration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefinitionSummary) -> dict:
    out: dict = {}
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "source_environment" in value:
        out["sourceEnvironment"] = value["source_environment"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "scope_tags" in value:
        import aws_sdk_mgn.types.scope_tags_map

        out["scopeTags"] = aws_sdk_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationDefinitionSummary:
    out: NetworkMigrationDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if "name" in data:
        out["name"] = data["name"]
    if "sourceEnvironment" in data:
        out["source_environment"] = data["sourceEnvironment"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "scopeTags" in data:
        import aws_sdk_mgn.types.scope_tags_map

        out["scope_tags"] = aws_sdk_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
