"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesUdtMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.keyspaces_cell

KeyspacesUdtMap: TypeAlias = dict[
    "str", "capo_keyspacesstreams.types.keyspaces_cell.KeyspacesCell"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: KeyspacesUdtMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_keyspacesstreams.types.keyspaces_cell

        out[key] = capo_keyspacesstreams.types.keyspaces_cell.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesUdtMap:
    out: KeyspacesUdtMap = {}
    for key, value in data.items():
        import capo_keyspacesstreams.types.keyspaces_cell

        out[key] = capo_keyspacesstreams.types.keyspaces_cell.deserialize_aws_json_1_0(
            value
        )
    return out
