"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphOutput``."""

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


class CreateGraphOutput(TypedDict):
    id: "aws_sdk_neptune_graph.types.graph_id.GraphId"
    """<p>The ID of the graph.</p>"""
    name: "aws_sdk_neptune_graph.types.graph_name.GraphName"
    """<p>The graph name. For example: <code>my-graph-1</code>.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    arn: "str"
    """<p>The ARN of the graph.</p>"""
    status: NotRequired["aws_sdk_neptune_graph.types.graph_status.GraphStatus"]
    """<p>The current status of the graph.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason the status was given.</p>"""
    create_time: NotRequired["datetime.datetime"]
    """<p>The time when the graph was created.</p>"""
    provisioned_memory: NotRequired[
        "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.</p> <p>Min = 16</p>"""
    endpoint: NotRequired["str"]
    """<p>The graph endpoint.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.</p> <note> <p>If enabling public connectivity for the first time, there will be a delay while it is enabled.</p> </note>"""
    vector_search_configuration: NotRequired[
        "aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
    ]
    """<p>The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.</p>"""
    replica_count: NotRequired["aws_sdk_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas in other AZs.</p> <p>Default: If not specified, the default value is 1.</p>"""
    kms_key_identifier: NotRequired["aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>Specifies the KMS key used to encrypt data in the new graph.</p>"""
    source_snapshot_id: NotRequired[
        "aws_sdk_neptune_graph.types.snapshot_id.SnapshotId"
    ]
    """<p>The ID of the source graph.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.</p>"""
    build_number: NotRequired["str"]
    """<p>The build number of the graph software.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphOutput) -> dict:
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


def deserialize_json(data: dict) -> CreateGraphOutput:
    out: CreateGraphOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateGraphOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGraphOutput.name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateGraphOutput.arn required")
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
