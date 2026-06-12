"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelImportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.imported_model_arn
    import aws_sdk_bedrock.types.imported_model_name
    import aws_sdk_bedrock.types.job_name
    import aws_sdk_bedrock.types.model_import_job_arn
    import aws_sdk_bedrock.types.model_import_job_status
    import aws_sdk_bedrock.types.timestamp


class ModelImportJobSummary(TypedDict):
    job_arn: "aws_sdk_bedrock.types.model_import_job_arn.ModelImportJobArn"
    """<p>The Amazon Resource Name (ARN) of the import job.</p>"""
    job_name: "aws_sdk_bedrock.types.job_name.JobName"
    """<p>The name of the import job.</p>"""
    status: "aws_sdk_bedrock.types.model_import_job_status.ModelImportJobStatus"
    """<p>The status of the imported job. </p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time when the import job was last modified.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The time import job was created.</p>"""
    end_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time when import job ended.</p>"""
    imported_model_arn: NotRequired[
        "aws_sdk_bedrock.types.imported_model_arn.ImportedModelArn"
    ]
    """<p>The Amazon resource Name (ARN) of the imported model.</p>"""
    imported_model_name: NotRequired[
        "aws_sdk_bedrock.types.imported_model_name.ImportedModelName"
    ]
    """<p>The name of the imported model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelImportJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    import aws_sdk_bedrock.types.model_import_job_status

    out["status"] = aws_sdk_bedrock.types.model_import_job_status.serialize_json(
        value["status"]
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastModifiedTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "end_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["endTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "imported_model_arn" in value:
        out["importedModelArn"] = value["imported_model_arn"]
    if "imported_model_name" in value:
        out["importedModelName"] = value["imported_model_name"]
    return out


def deserialize_json(data: dict) -> ModelImportJobSummary:
    out: ModelImportJobSummary = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("ModelImportJobSummary.job_arn required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("ModelImportJobSummary.job_name required")
    if "status" in data:
        import aws_sdk_bedrock.types.model_import_job_status

        out["status"] = aws_sdk_bedrock.types.model_import_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ModelImportJobSummary.status required")
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_modified_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ModelImportJobSummary.creation_time required")
    if "endTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["end_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "importedModelArn" in data:
        out["imported_model_arn"] = data["importedModelArn"]
    if "importedModelName" in data:
        out["imported_model_name"] = data["importedModelName"]
    return out
