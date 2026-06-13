"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ResetGraphOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_neptune_graph.types.graph_id
    import aws_sdk_neptune_graph.types.graph_name
    import aws_sdk_neptune_graph.types.graph_status
    import aws_sdk_neptune_graph.types.kms_key_arn
    import aws_sdk_neptune_graph.types.provisioned_memory
    import aws_sdk_neptune_graph.types.replica_count
    import aws_sdk_neptune_graph.types.snapshot_id
    import aws_sdk_neptune_graph.types.vector_search_configuration


class ResetGraphOutput(TypedDict):
    id: "aws_sdk_neptune_graph.types.graph_id.GraphId"
    """<p>The unique identifier of the graph.</p>"""
    name: "aws_sdk_neptune_graph.types.graph_name.GraphName"
    """<p>The name of the graph.</p>"""
    arn: "str"
    """<p>The ARN associated with the graph.</p>"""
    status: NotRequired["aws_sdk_neptune_graph.types.graph_status.GraphStatus"]
    """<p>The status of the graph.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason that the graph has this status.</p>"""
    create_time: NotRequired["datetime.datetime"]
    """<p>The time at which the graph was created.</p>"""
    provisioned_memory: NotRequired[
        "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.</p>"""
    endpoint: NotRequired["str"]
    """<p>The graph endpoint.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>If <code>true</code>, the graph has a public endpoint, otherwise not.</p>"""
    vector_search_configuration: NotRequired[
        "aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
    ]
    replica_count: NotRequired["aws_sdk_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas for the graph.</p>"""
    kms_key_identifier: NotRequired["aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>The ID of the KMS key used to encrypt and decrypt graph data.</p>"""
    source_snapshot_id: NotRequired[
        "aws_sdk_neptune_graph.types.snapshot_id.SnapshotId"
    ]
    """<p>The ID of the snapshot from which the graph was created, if any.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>If <code>true</code>, deletion protection is enabled for the graph.</p>"""
    build_number: NotRequired["str"]
    """<p>The build number of the graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetGraphOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_neptune_graph.types.graph_status

        out["status"] = aws_sdk_neptune_graph.types.graph_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "create_time" in value:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["createTime"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.serialize_json(
                value["create_time"]
            )
        )
    if "provisioned_memory" in value:
        out["provisionedMemory"] = value["provisioned_memory"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    if "vector_search_configuration" in value:
        import aws_sdk_neptune_graph.types.vector_search_configuration

        out["vectorSearchConfiguration"] = (
            aws_sdk_neptune_graph.types.vector_search_configuration.serialize_json(
                value["vector_search_configuration"]
            )
        )
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "source_snapshot_id" in value:
        out["sourceSnapshotId"] = value["source_snapshot_id"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "build_number" in value:
        out["buildNumber"] = value["build_number"]
    return out


def deserialize_json(data: dict) -> ResetGraphOutput:
    out: ResetGraphOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ResetGraphOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ResetGraphOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ResetGraphOutput.arn required")
    if "status" in data:
        import aws_sdk_neptune_graph.types.graph_status

        out["status"] = aws_sdk_neptune_graph.types.graph_status.deserialize_json(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "createTime" in data:
        import aws_sdk_neptune_graph.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_neptune_graph.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    if "provisionedMemory" in data:
        out["provisioned_memory"] = data["provisionedMemory"]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "publicConnectivity" in data:
        out["public_connectivity"] = data["publicConnectivity"]
    if "vectorSearchConfiguration" in data:
        import aws_sdk_neptune_graph.types.vector_search_configuration

        out["vector_search_configuration"] = (
            aws_sdk_neptune_graph.types.vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    if "replicaCount" in data:
        out["replica_count"] = data["replicaCount"]
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if "sourceSnapshotId" in data:
        out["source_snapshot_id"] = data["sourceSnapshotId"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "buildNumber" in data:
        out["build_number"] = data["buildNumber"]
    return out
