"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCellMap``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition

KeyspacesCellMap: TypeAlias = list["aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition.KeyspacesCellMapDefinition"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCellMap) -> list:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition
    out: list = []
    for item in value:
        out.append(aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> KeyspacesCellMap:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition
    out: KeyspacesCellMap = []
    for item in data:
        out.append(aws_sdk_keyspacesstreams.types.keyspaces_cell_map_definition.deserialize_aws_json_1_0(item))
    return out