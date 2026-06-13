"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCellList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell

KeyspacesCellList: TypeAlias = list[
    "aws_sdk_keyspacesstreams.types.keyspaces_cell.KeyspacesCell"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCellList) -> list:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell

    out: list = []
    for item in value:
        out.append(
            aws_sdk_keyspacesstreams.types.keyspaces_cell.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KeyspacesCellList:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell

    out: KeyspacesCellList = []
    for item in data:
        out.append(
            aws_sdk_keyspacesstreams.types.keyspaces_cell.deserialize_aws_json_1_0(item)
        )
    return out
