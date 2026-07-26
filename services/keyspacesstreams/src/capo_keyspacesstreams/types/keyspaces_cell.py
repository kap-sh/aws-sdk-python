"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCell``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspacesstreams.types.keyspaces_cell_value
    import capo_keyspacesstreams.types.keyspaces_metadata


class KeyspacesCell(TypedDict, closed=True):
    value: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_cell_value.KeyspacesCellValue"
    ]
    """<p>The value stored in this cell, which can be of various data types supported by Amazon Keyspaces.</p>"""
    metadata: NotRequired[
        "capo_keyspacesstreams.types.keyspaces_metadata.KeyspacesMetadata"
    ]
    """<p>Metadata associated with this cell, such as time-to-live (TTL) expiration time and write timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCell) -> dict:
    out: dict = {}
    if "value" in value:
        import capo_keyspacesstreams.types.keyspaces_cell_value

        out["value"] = (
            capo_keyspacesstreams.types.keyspaces_cell_value.serialize_aws_json_1_0(
                value["value"]
            )
        )
    if "metadata" in value:
        import capo_keyspacesstreams.types.keyspaces_metadata

        out["metadata"] = (
            capo_keyspacesstreams.types.keyspaces_metadata.serialize_aws_json_1_0(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyspacesCell:
    out: KeyspacesCell = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_keyspacesstreams.types.keyspaces_cell_value

        out["value"] = (
            capo_keyspacesstreams.types.keyspaces_cell_value.deserialize_aws_json_1_0(
                data["value"]
            )
        )
    if "metadata" in data:
        import capo_keyspacesstreams.types.keyspaces_metadata

        out["metadata"] = (
            capo_keyspacesstreams.types.keyspaces_metadata.deserialize_aws_json_1_0(
                data["metadata"]
            )
        )
    return out
