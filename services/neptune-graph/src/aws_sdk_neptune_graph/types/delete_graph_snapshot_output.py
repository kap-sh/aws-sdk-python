"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeleteGraphSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_neptune_graph.types.graph_id
    import aws_sdk_neptune_graph.types.kms_key_arn
    import aws_sdk_neptune_graph.types.snapshot_id
    import aws_sdk_neptune_graph.types.snapshot_name
    import aws_sdk_neptune_graph.types.snapshot_status


class DeleteGraphSnapshotOutput(TypedDict, closed=True):
    id: "aws_sdk_neptune_graph.types.snapshot_id.SnapshotId"
    """<p>The unique identifier of the graph snapshot.</p>"""
    name: "aws_sdk_neptune_graph.types.snapshot_name.SnapshotName"
    """<p>The snapshot name. For example: <code>my-snapshot-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    arn: "str"
    """<p>The ARN of the graph snapshot.</p>"""
    source_graph_id: NotRequired["aws_sdk_neptune_graph.types.graph_id.GraphId"]
    """<p>The graph identifier for the graph from which the snapshot was created.</p>"""
    snapshot_create_time: NotRequired["datetime.datetime"]
    """<p>The time when the snapshot was created.</p>"""
    status: NotRequired["aws_sdk_neptune_graph.types.snapshot_status.SnapshotStatus"]
    """<p>The status of the graph snapshot.</p>"""
    kms_key_identifier: NotRequired["aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>The ID of the KMS key used to encrypt and decrypt the snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphSnapshotOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "source_graph_id" in value:
        out["sourceGraphId"] = value["source_graph_id"]
    if "snapshot_create_time" in value:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["snapshotCreateTime"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.serialize_json(
                value["snapshot_create_time"]
            )
        )
    if "status" in value:
        import aws_sdk_neptune_graph.types.snapshot_status

        out["status"] = aws_sdk_neptune_graph.types.snapshot_status.serialize_json(
            value["status"]
        )
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteGraphSnapshotOutput:
    out: DeleteGraphSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteGraphSnapshotOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteGraphSnapshotOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteGraphSnapshotOutput.arn required")
    if "sourceGraphId" in data:
        out["source_graph_id"] = data["sourceGraphId"]
    if "snapshotCreateTime" in data:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["snapshot_create_time"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["snapshotCreateTime"]
            )
        )
    if "status" in data:
        import aws_sdk_neptune_graph.types.snapshot_status

        out["status"] = aws_sdk_neptune_graph.types.snapshot_status.deserialize_json(
            data["status"]
        )
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    return out
