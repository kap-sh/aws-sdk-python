"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateNetworkMigrationMapperSegmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.segment_id


class UpdateNetworkMigrationMapperSegmentRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    network_migration_execution_id: (
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    segment_id: "aws_sdk_mgn.types.segment_id.SegmentID"
    """<p>The unique identifier of the segment to update.</p>"""
    scope_tags: NotRequired["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkMigrationMapperSegmentRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["segmentID"] = value["segment_id"]
    if "scope_tags" in value:
        import aws_sdk_mgn.types.scope_tags_map

        out["scopeTags"] = aws_sdk_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateNetworkMigrationMapperSegmentRequest:
    out: UpdateNetworkMigrationMapperSegmentRequest = {}  # type: ignore[typeddict-item]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        raise DeserializationError(
            "UpdateNetworkMigrationMapperSegmentRequest.network_migration_definition_id required"
        )
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        raise DeserializationError(
            "UpdateNetworkMigrationMapperSegmentRequest.network_migration_execution_id required"
        )
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    else:
        raise DeserializationError(
            "UpdateNetworkMigrationMapperSegmentRequest.segment_id required"
        )
    if "scopeTags" in data:
        import aws_sdk_mgn.types.scope_tags_map

        out["scope_tags"] = aws_sdk_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
