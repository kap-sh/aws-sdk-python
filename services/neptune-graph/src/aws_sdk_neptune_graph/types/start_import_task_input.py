"""Generated from Smithy shape ``com.amazonaws.neptunegraph#StartImportTaskInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.blank_node_handling
    import aws_sdk_neptune_graph.types.format
    import aws_sdk_neptune_graph.types.graph_identifier
    import aws_sdk_neptune_graph.types.import_options
    import aws_sdk_neptune_graph.types.parquet_type
    import aws_sdk_neptune_graph.types.role_arn


class StartImportTaskInput(TypedDict):
    import_options: NotRequired[
        "aws_sdk_neptune_graph.types.import_options.ImportOptions"
    ]
    fail_on_error: NotRequired["bool"]
    """<p>If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.</p>"""
    source: "str"
    """<p>A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>"""
    format: NotRequired["aws_sdk_neptune_graph.types.format.Format"]
    """<p>Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identifies the openCypher load format.</p>"""
    parquet_type: NotRequired["aws_sdk_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    blank_node_handling: NotRequired[
        "aws_sdk_neptune_graph.types.blank_node_handling.BlankNodeHandling"
    ]
    r"""<p>The method to handle blank nodes in the dataset. Currently, only <code>convertToIri</code> is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is <code>ntriples</code>. For more information, see <a href=\"https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling\">Handling RDF values</a>.</p>"""
    graph_identifier: "aws_sdk_neptune_graph.types.graph_identifier.GraphIdentifier"
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    role_arn: "aws_sdk_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportTaskInput) -> dict:
    out: dict = {}
    if "import_options" in value:
        import aws_sdk_neptune_graph.types.import_options

        out["importOptions"] = (
            aws_sdk_neptune_graph.types.import_options.serialize_json(
                value["import_options"]
            )
        )
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


def deserialize_json(data: dict) -> StartImportTaskInput:
    out: StartImportTaskInput = {}  # type: ignore[typeddict-item]
    if "importOptions" in data:
        import aws_sdk_neptune_graph.types.import_options

        out["import_options"] = (
            aws_sdk_neptune_graph.types.import_options.deserialize_json(
                data["importOptions"]
            )
        )
    if "failOnError" in data:
        out["fail_on_error"] = data["failOnError"]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("StartImportTaskInput.source required")
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
        raise DeserializationError("StartImportTaskInput.role_arn required")
    return out
