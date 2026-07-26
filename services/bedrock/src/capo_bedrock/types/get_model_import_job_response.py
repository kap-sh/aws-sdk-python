"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.error_message
    import capo_bedrock.types.imported_model_arn
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.model_import_job_arn
    import capo_bedrock.types.model_import_job_status
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.vpc_config


class GetModelImportJobResponse(TypedDict, closed=True):
    job_arn: NotRequired["capo_bedrock.types.model_import_job_arn.ModelImportJobArn"]
    """<p>The Amazon Resource Name (ARN) of the import job.</p>"""
    job_name: NotRequired["capo_bedrock.types.job_name.JobName"]
    """<p>The name of the import job.</p>"""
    imported_model_name: NotRequired[
        "capo_bedrock.types.imported_model_name.ImportedModelName"
    ]
    """<p>The name of the imported model.</p>"""
    imported_model_arn: NotRequired[
        "capo_bedrock.types.imported_model_arn.ImportedModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the imported model.</p>"""
    role_arn: NotRequired["capo_bedrock.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with this job.</p>"""
    model_data_source: NotRequired[
        "capo_bedrock.types.model_data_source.ModelDataSource"
    ]
    """<p>The data source for the imported model.</p>"""
    status: NotRequired[
        "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
    ]
    """<p>The status of the job. A successful job transitions from in-progress to completed when the imported model is ready to use. If the job failed, the failure message contains information about why the job failed.</p>"""
    failure_message: NotRequired["capo_bedrock.types.error_message.ErrorMessage"]
    """<p>Information about why the import job failed.</p>"""
    creation_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time the resource was created.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time the resource was last modified.</p>"""
    end_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the resource transitioned to terminal state.</p>"""
    vpc_config: NotRequired["capo_bedrock.types.vpc_config.VpcConfig"]
    """<p>The Virtual Private Cloud (VPC) configuration of the import model job.</p>"""
    imported_model_kms_key_arn: NotRequired["capo_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The imported model is encrypted at rest using this key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelImportJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "imported_model_name" in value:
        out["importedModelName"] = value["imported_model_name"]
    if "imported_model_arn" in value:
        out["importedModelArn"] = value["imported_model_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "model_data_source" in value:
        import capo_bedrock.types.model_data_source

        out["modelDataSource"] = capo_bedrock.types.model_data_source.serialize_json(
            value["model_data_source"]
        )
    if "status" in value:
        import capo_bedrock.types.model_import_job_status

        out["status"] = capo_bedrock.types.model_import_job_status.serialize_json(
            value["status"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    if "creation_time" in value:
        import capo_bedrock.types.timestamp

        out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import capo_bedrock.types.timestamp

        out["endTime"] = capo_bedrock.types.timestamp.serialize_json(value["end_time"])
    if "vpc_config" in value:
        import capo_bedrock.types.vpc_config

        out["vpcConfig"] = capo_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "imported_model_kms_key_arn" in value:
        out["importedModelKmsKeyArn"] = value["imported_model_kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetModelImportJobResponse:
    out: GetModelImportJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "importedModelName" in data:
        out["imported_model_name"] = data["importedModelName"]
    if "importedModelArn" in data:
        out["imported_model_arn"] = data["importedModelArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "modelDataSource" in data:
        import capo_bedrock.types.model_data_source

        out["model_data_source"] = (
            capo_bedrock.types.model_data_source.deserialize_json(
                data["modelDataSource"]
            )
        )
    if "status" in data:
        import capo_bedrock.types.model_import_job_status

        out["status"] = capo_bedrock.types.model_import_job_status.deserialize_json(
            data["status"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "creationTime" in data:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastModifiedTime" in data:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if "endTime" in data:
        import capo_bedrock.types.timestamp

        out["end_time"] = capo_bedrock.types.timestamp.deserialize_json(data["endTime"])
    if "vpcConfig" in data:
        import capo_bedrock.types.vpc_config

        out["vpc_config"] = capo_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if "importedModelKmsKeyArn" in data:
        out["imported_model_kms_key_arn"] = data["importedModelKmsKeyArn"]
    return out
