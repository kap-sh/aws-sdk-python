"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExportTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_format
    import capo_neptune_graph.types.export_task_id
    import capo_neptune_graph.types.export_task_status
    import capo_neptune_graph.types.graph_id
    import capo_neptune_graph.types.kms_key_arn
    import capo_neptune_graph.types.parquet_type
    import capo_neptune_graph.types.role_arn


class ExportTaskSummary(TypedDict, closed=True):
    graph_id: "capo_neptune_graph.types.graph_id.GraphId"
    """<p>The source graph identifier of the export task.</p>"""
    role_arn: "capo_neptune_graph.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that will allow the data to be exported to the destination.</p>"""
    task_id: "capo_neptune_graph.types.export_task_id.ExportTaskId"
    """<p>The unique identifier of the export task.</p>"""
    status: "capo_neptune_graph.types.export_task_status.ExportTaskStatus"
    """<p>The current status of the export task.</p>"""
    format: "capo_neptune_graph.types.export_format.ExportFormat"
    """<p>The format of the export task.</p>"""
    destination: "str"
    """<p>The Amazon S3 URI of the export task where data will be exported to.</p>"""
    kms_key_identifier: "capo_neptune_graph.types.kms_key_arn.KmsKeyArn"
    """<p>The KMS key identifier of the export task.</p>"""
    parquet_type: NotRequired["capo_neptune_graph.types.parquet_type.ParquetType"]
    """<p>The parquet type of the export task.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason that the export task has this status value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskSummary) -> dict:
    out: dict = {}
    out["graphId"] = value["graph_id"]
    out["roleArn"] = value["role_arn"]
    out["taskId"] = value["task_id"]
    import capo_neptune_graph.types.export_task_status

    out["status"] = capo_neptune_graph.types.export_task_status.serialize_json(
        value["status"]
    )
    import capo_neptune_graph.types.export_format

    out["format"] = capo_neptune_graph.types.export_format.serialize_json(
        value["format"]
    )
    out["destination"] = value["destination"]
    out["kmsKeyIdentifier"] = value["kms_key_identifier"]
    if "parquet_type" in value:
        import capo_neptune_graph.types.parquet_type

        out["parquetType"] = capo_neptune_graph.types.parquet_type.serialize_json(
            value["parquet_type"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> ExportTaskSummary:
    out: ExportTaskSummary = {}  # type: ignore[typeddict-item]
    if "graphId" in data:
        out["graph_id"] = data["graphId"]
    else:
        raise DeserializationError("ExportTaskSummary.graph_id required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ExportTaskSummary.role_arn required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("ExportTaskSummary.task_id required")
    if "status" in data:
        import capo_neptune_graph.types.export_task_status

        out["status"] = capo_neptune_graph.types.export_task_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ExportTaskSummary.status required")
    if "format" in data:
        import capo_neptune_graph.types.export_format

        out["format"] = capo_neptune_graph.types.export_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("ExportTaskSummary.format required")
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("ExportTaskSummary.destination required")
    if "kmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["kmsKeyIdentifier"]
    else:
        raise DeserializationError("ExportTaskSummary.kms_key_identifier required")
    if "parquetType" in data:
        import capo_neptune_graph.types.parquet_type

        out["parquet_type"] = capo_neptune_graph.types.parquet_type.deserialize_json(
            data["parquetType"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
