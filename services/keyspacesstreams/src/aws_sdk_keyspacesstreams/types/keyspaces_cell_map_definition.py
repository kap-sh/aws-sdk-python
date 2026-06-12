"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCellMapDefinition``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_value
    import aws_sdk_keyspacesstreams.types.keyspaces_metadata

class KeyspacesCellMapDefinition(TypedDict):
    key: NotRequired["aws_sdk_keyspacesstreams.types.keyspaces_cell_value.KeyspacesCellValue"]
    """<p>The key of this map entry in the Amazon Keyspaces cell.</p>"""
    value: NotRequired["aws_sdk_keyspacesstreams.types.keyspaces_cell_value.KeyspacesCellValue"]
    """<p>The value associated with the key in this map entry.</p>"""
    metadata: NotRequired["aws_sdk_keyspacesstreams.types.keyspaces_metadata.KeyspacesMetadata"]
    """<p>Metadata for this specific key-value pair within the map, such as timestamps and TTL information.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCellMapDefinition) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value
        out["key"] = aws_sdk_keyspacesstreams.types.keyspaces_cell_value.serialize_aws_json_1_0(value["key"])
    if "value" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value
        out["value"] = aws_sdk_keyspacesstreams.types.keyspaces_cell_value.serialize_aws_json_1_0(value["value"])
    if "metadata" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_metadata
        out["metadata"] = aws_sdk_keyspacesstreams.types.keyspaces_metadata.serialize_aws_json_1_0(value["metadata"])
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesCellMapDefinition:
    out: KeyspacesCellMapDefinition = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value
        out["key"] = aws_sdk_keyspacesstreams.types.keyspaces_cell_value.deserialize_aws_json_1_0(data["key"])
    if "value" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value
        out["value"] = aws_sdk_keyspacesstreams.types.keyspaces_cell_value.deserialize_aws_json_1_0(data["value"])
    if "metadata" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_metadata
        out["metadata"] = aws_sdk_keyspacesstreams.types.keyspaces_metadata.deserialize_aws_json_1_0(data["metadata"])
    return out