"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.snapshot_name
    import aws_sdk_neptune_graph.types.tag_map


class CreateGraphSnapshotInput(TypedDict, closed=True):
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    snapshot_name: "aws_sdk_neptune_graph.types.snapshot_name.SnapshotName"
    """<p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    tags: NotRequired["aws_sdk_neptune_graph.types.tag_map.TagMap"]
    """<p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphSnapshotInput) -> dict:
    out: dict = {}
    out["graphIdentifier"] = value["graph_identifier"]
    out["snapshotName"] = value["snapshot_name"]
    if "tags" in value:
        import aws_sdk_neptune_graph.types.tag_map

        out["tags"] = aws_sdk_neptune_graph.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateGraphSnapshotInput:
    out: CreateGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    if "graphIdentifier" in data:
        out["graph_identifier"] = data["graphIdentifier"]
    else:
        raise DeserializationError("CreateGraphSnapshotInput.graph_identifier required")
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    else:
        raise DeserializationError("CreateGraphSnapshotInput.snapshot_name required")
    if "tags" in data:
        import aws_sdk_neptune_graph.types.tag_map

        out["tags"] = aws_sdk_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    return out
