"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesKeysMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_value

KeyspacesKeysMap: TypeAlias = dict[
    "str", "aws_sdk_keyspacesstreams.types.keyspaces_cell_value.KeyspacesCellValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: KeyspacesKeysMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value

        out[key] = (
            aws_sdk_keyspacesstreams.types.keyspaces_cell_value.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesKeysMap:
    out: KeyspacesKeysMap = {}
    for key, value in data.items():
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_value

        out[key] = (
            aws_sdk_keyspacesstreams.types.keyspaces_cell_value.deserialize_aws_json_1_0(
                value
            )
        )
    return out
