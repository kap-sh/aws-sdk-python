"""Generated from Smithy shape ``com.amazonaws.neptunegraph#CreateGraphUsingImportTaskOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.format
    import aws_sdk_neptune_graph.types.graph_id
    import aws_sdk_neptune_graph.types.import_options
    import aws_sdk_neptune_graph.types.import_task_status
    import aws_sdk_neptune_graph.types.parquet_type
    import aws_sdk_neptune_graph.types.role_arn
    import aws_sdk_neptune_graph.types.task_id


class CreateGraphUsingImportTaskOutput(TypedDict):
    graph_id: NotRequired["aws_sdk_neptune_graph.types.graph_id.GraphId"]
    """<p>The unique identifier of the Neptune Analytics graph.</p>"""
    task_id: "aws_sdk_neptune_graph.types.task_id.TaskId"
    """<p>The unique identifier of the import task.</p>"""
    source: "str"
    """<p>A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.</p>"""
    format: NotRequired["aws_sdk_neptune_graph.types.format.Format"]
    r"""<p>Specifies the format of S3 data to be imported. Valid values are <code>CSV</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html\">Gremlin CSV format</a>, <code>OPENCYPHER</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html\">openCypher load format</a>, or <code>ntriples</code>, which identifies the <a href=\"https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html\">RDF n-triples</a> format.</p>"""
    parquet_type: NotRequired["aws_sdk_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the import task.</p>"""
    role_arn: "aws_sdk_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow access to the data that is to be imported.</p>"""
    status: "aws_sdk_neptune_graph.types.import_task_status.ImportTaskStatus"
    """<p>The status of the import task.</p>"""
    import_options: NotRequired[
        "aws_sdk_neptune_graph.types.import_options.ImportOptions"
    ]
    """<p>Contains options for controlling the import process. For example, if the <code>failOnError</code> key is set to <code>false</code>, the import skips problem data and attempts to continue (whereas if set to <code>true</code>, the default, or if omitted, the import operation halts immediately when an error is encountered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphUsingImportTaskOutput) -> dict:
    out: dict = {}
    if "graph_id" in value:
        out["graphId"] = value["graph_id"]
    out["taskId"] = value["task_id"]
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
    out["roleArn"] = value["role_arn"]
    import aws_sdk_neptune_graph.types.import_task_status

    out["status"] = aws_sdk_neptune_graph.types.import_task_status.serialize_json(
        value["status"]
    )
    if "import_options" in value:
        import aws_sdk_neptune_graph.types.import_options

        out["importOptions"] = (
            aws_sdk_neptune_graph.types.import_options.serialize_json(
                value["import_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateGraphUsingImportTaskOutput:
    out: CreateGraphUsingImportTaskOutput = {}  # type: ignore[typeddict-item]
    if "graphId" in data:
        out["graph_id"] = data["graphId"]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("CreateGraphUsingImportTaskOutput.task_id required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("CreateGraphUsingImportTaskOutput.source required")
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
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateGraphUsingImportTaskOutput.role_arn required")
    if "status" in data:
        import aws_sdk_neptune_graph.types.import_task_status

        out["status"] = aws_sdk_neptune_graph.types.import_task_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateGraphUsingImportTaskOutput.status required")
    if "importOptions" in data:
        import aws_sdk_neptune_graph.types.import_options

        out["import_options"] = (
            aws_sdk_neptune_graph.types.import_options.deserialize_json(
                data["importOptions"]
            )
        )
    return out
