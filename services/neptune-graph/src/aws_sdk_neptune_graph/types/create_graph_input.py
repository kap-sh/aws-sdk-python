"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_neptune_graph.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_name
    import aws_sdk_neptune_graph.types.kms_key_arn
    import aws_sdk_neptune_graph.types.provisioned_memory
    import aws_sdk_neptune_graph.types.replica_count
    import aws_sdk_neptune_graph.types.tag_map
    import aws_sdk_neptune_graph.types.vector_search_configuration

class CreateGraphInput(TypedDict):
    graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName"
    """<p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    tags: NotRequired["aws_sdk_neptune_graph.types.tag_map.TagMap"]
    """<p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable.</p>"""
    kms_key_identifier: NotRequired["aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>Specifies a KMS key to use to encrypt data in the new graph.</p>"""
    vector_search_configuration: NotRequired["aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"]
    """<p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535</p>"""
    replica_count: NotRequired["aws_sdk_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas in other AZs. Min =0, Max = 2, Default = 1.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>"""
    provisioned_memory: "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    """<p>The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphInput) -> dict:
    out: dict = {}
    out["graphName"] = value["graph_name"]
    if "tags" in value:
        import aws_sdk_neptune_graph.types.tag_map
        out["tags"] = aws_sdk_neptune_graph.types.tag_map.serialize_json(value["tags"])
    if "public_connectivity" in value:
        out["publicConnectivity"] = value["public_connectivity"]
    if "kms_key_identifier" in value:
        out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "vector_search_configuration" in value:
        import aws_sdk_neptune_graph.types.vector_search_configuration
        out["vectorSearchConfiguration"] = aws_sdk_neptune_graph.types.vector_search_configuration.serialize_json(value["vector_search_configuration"])
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    out["provisionedMemory"] = value["provisioned_memory"]
    return out


def deserialize_json(data: dict) -> CreateGraphInput:
    out: CreateGraphInput = {}  # type: ignore[typeddict-item]
    if "graphName" in data:
        out["graph_name"] = data["graphName"]
    else:
        raise DeserializationError("CreateGraphInput.graph_name required")
    if "tags" in data:
        import aws_sdk_neptune_graph.types.tag_map
        out["tags"] = aws_sdk_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    if "publicConnectivity" in data:
        out["public_connectivity"] = data["publicConnectivity"]
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if "vectorSearchConfiguration" in data:
        import aws_sdk_neptune_graph.types.vector_search_configuration
        out["vector_search_configuration"] = aws_sdk_neptune_graph.types.vector_search_configuration.deserialize_json(data["vectorSearchConfiguration"])
    if "replicaCount" in data:
        out["replica_count"] = data["replicaCount"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "provisionedMemory" in data:
        out["provisioned_memory"] = data["provisionedMemory"]
    else:
        raise DeserializationError("CreateGraphInput.provisioned_memory required")
    return out