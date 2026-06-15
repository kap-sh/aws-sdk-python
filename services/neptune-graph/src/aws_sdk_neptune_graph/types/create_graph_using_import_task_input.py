"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphUsingImportTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.blank_node_handling
    import aws_sdk_neptune_graph.types.format
    import aws_sdk_neptune_graph.types.graph_name
    import aws_sdk_neptune_graph.types.import_options
    import aws_sdk_neptune_graph.types.kms_key_arn
    import aws_sdk_neptune_graph.types.parquet_type
    import aws_sdk_neptune_graph.types.provisioned_memory
    import aws_sdk_neptune_graph.types.replica_count
    import aws_sdk_neptune_graph.types.role_arn
    import aws_sdk_neptune_graph.types.tag_map
    import aws_sdk_neptune_graph.types.vector_search_configuration


class CreateGraphUsingImportTaskInput(TypedDict):
    graph_name: "aws_sdk_neptune_graph.types.graph_name.GraphName"
    """<p>A name for the new Neptune Analytics graph to be created.</p> <p>The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.</p>"""
    tags: NotRequired["aws_sdk_neptune_graph.types.tag_map.TagMap"]
    """<p>Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.</p>"""
    public_connectivity: NotRequired["bool"]
    """<p>Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (<code>true</code> to enable, or <code>false</code> to disable).</p>"""
    kms_key_identifier: NotRequired["aws_sdk_neptune_graph.types.kms_key_arn.KmsKeyArn"]
    """<p>Specifies a KMS key to use to encrypt data imported into the new graph.</p>"""
    vector_search_configuration: NotRequired[
        "aws_sdk_neptune_graph.types.vector_search_configuration.VectorSearchConfiguration"
    ]
    """<p>Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as <code>dimension=</code>value. Max = 65,535 </p>"""
    replica_count: NotRequired["aws_sdk_neptune_graph.types.replica_count.ReplicaCount"]
    """<p>The number of replicas in other AZs to provision on the new graph after import. Default = 0, Min = 0, Max = 2.</p> <important> <p> Additional charges equivalent to the m-NCUs selected for the graph apply for each replica. </p> </important>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (<code>true</code> or <code>false</code>).</p>"""
    import_options: NotRequired[
        "aws_sdk_neptune_graph.types.import_options.ImportOptions"
    ]
    """<p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>"""
    max_provisioned_memory: NotRequired[
        "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.</p> <p> If both the minimum and maximum values are specified, the final <code>provisioned-memory</code> will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.</p>"""
    min_provisioned_memory: NotRequired[
        "aws_sdk_neptune_graph.types.provisioned_memory.ProvisionedMemory"
    ]
    """<p>The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16</p>"""
    fail_on_error: NotRequired["bool"]
    """<p>If set to <code>true</code>, the task halts when an import error is encountered. If set to <code>false</code>, the task skips the data that caused the error and continues if possible.</p>"""
    source: "str"
    """<p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>"""
    format: NotRequired["aws_sdk_neptune_graph.types.format.Format"]
    r"""<p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html\">Gremlin CSV format</a>, <code>OPEN_CYPHER</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html\">openCypher load format</a>, or <code>ntriples</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html\">RDF n-triples</a> format.</p>"""
    parquet_type: NotRequired["aws_sdk_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    blank_node_handling: NotRequired[
        "aws_sdk_neptune_graph.types.blank_node_handling.BlankNodeHandling"
    ]
    r"""<p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href=\"https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling\">Handling RDF values</a>.</p>"""
    role_arn: "aws_sdk_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphUsingImportTaskInput) -> dict:
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

        out["vectorSearchConfiguration"] = (
            aws_sdk_neptune_graph.types.vector_search_configuration.serialize_json(
                value["vector_search_configuration"]
            )
        )
    if "replica_count" in value:
        out["replicaCount"] = value["replica_count"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "import_options" in value:
        import aws_sdk_neptune_graph.types.import_options

        out["importOptions"] = (
            aws_sdk_neptune_graph.types.import_options.serialize_json(
                value["import_options"]
            )
        )
    if "max_provisioned_memory" in value:
        out["maxProvisionedMemory"] = value["max_provisioned_memory"]
    if "min_provisioned_memory" in value:
        out["minProvisionedMemory"] = value["min_provisioned_memory"]
    if "fail_on_error" in value:
        out["failOnError"] = value["fail_on_error"]
    out["source"] = value["source"]
    if "format" in value:
        import aws_sdk_neptune_graph.types.format

        out["format"] = aws_sdk_neptune_graph.types.format.serialize_json(
            value["format"]
        )
    if "parquet_type" in value:
        import aws_sdk_neptune_graph.types.parquet_type

        out["parquetType"] = aws_sdk_neptune_graph.types.parquet_type.serialize_json(
            value["parquet_type"]
        )
    if "blank_node_handling" in value:
        import aws_sdk_neptune_graph.types.blank_node_handling

        out["blankNodeHandling"] = (
            aws_sdk_neptune_graph.types.blank_node_handling.serialize_json(
                value["blank_node_handling"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CreateGraphUsingImportTaskInput:
    out: CreateGraphUsingImportTaskInput = {}  # type: ignore[typeddict-item]
    if "graphName" in data:
        out["graph_name"] = data["graphName"]
    else:
        raise DeserializationError(
            "CreateGraphUsingImportTaskInput.graph_name required"
        )
    if "tags" in data:
        import aws_sdk_neptune_graph.types.tag_map

        out["tags"] = aws_sdk_neptune_graph.types.tag_map.deserialize_json(data["tags"])
    if "publicConnectivity" in data:
        out["public_connectivity"] = data["publicConnectivity"]
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    if "vectorSearchConfiguration" in data:
        import aws_sdk_neptune_graph.types.vector_search_configuration

        out["vector_search_configuration"] = (
            aws_sdk_neptune_graph.types.vector_search_configuration.deserialize_json(
                data["vectorSearchConfiguration"]
            )
        )
    if "replicaCount" in data:
        out["replica_count"] = data["replicaCount"]
    if "deletionProtection" in data:
        out["deletion_protection"] = data["deletionProtection"]
    if "importOptions" in data:
        import aws_sdk_neptune_graph.types.import_options

        out["import_options"] = (
            aws_sdk_neptune_graph.types.import_options.deserialize_json(
                data["importOptions"]
            )
        )
    if "maxProvisionedMemory" in data:
        out["max_provisioned_memory"] = data["maxProvisionedMemory"]
    if "minProvisionedMemory" in data:
        out["min_provisioned_memory"] = data["minProvisionedMemory"]
    if "failOnError" in data:
        out["fail_on_error"] = data["failOnError"]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("CreateGraphUsingImportTaskInput.source required")
    if "format" in data:
        import aws_sdk_neptune_graph.types.format

        out["format"] = aws_sdk_neptune_graph.types.format.deserialize_json(
            data["format"]
        )
    if "parquetType" in data:
        import aws_sdk_neptune_graph.types.parquet_type

        out["parquet_type"] = aws_sdk_neptune_graph.types.parquet_type.deserialize_json(
            data["parquetType"]
        )
    if "blankNodeHandling" in data:
        import aws_sdk_neptune_graph.types.blank_node_handling

        out["blank_node_handling"] = (
            aws_sdk_neptune_graph.types.blank_node_handling.deserialize_json(
                data["blankNodeHandling"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateGraphUsingImportTaskInput.role_arn required")
    return out
