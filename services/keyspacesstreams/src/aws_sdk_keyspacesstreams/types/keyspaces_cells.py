"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCells``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell

KeyspacesCells: TypeAlias = dict[
    "str", "aws_sdk_keyspacesstreams.types.keyspaces_cell.KeyspacesCell"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: KeyspacesCells) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_keyspacesstreams.types.keyspaces_cell

        out[key] = aws_sdk_keyspacesstreams.types.keyspaces_cell.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesCells:
    out: KeyspacesCells = {}
    for key, value in data.items():
        import aws_sdk_keyspacesstreams.types.keyspaces_cell

        out[key] = (
            aws_sdk_keyspacesstreams.types.keyspaces_cell.deserialize_aws_json_1_0(
                value
            )
        )
    return out
