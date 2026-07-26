"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePackagingJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_packaging_job_arn
    import capo_sagemaker.types.edge_packaging_job_status
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.timestamp


class EdgePackagingJobSummary(TypedDict, closed=True):
    edge_packaging_job_arn: NotRequired[
        "capo_sagemaker.types.edge_packaging_job_arn.EdgePackagingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the edge packaging job.</p>"""
    edge_packaging_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the edge packaging job.</p>"""
    edge_packaging_job_status: NotRequired[
        "capo_sagemaker.types.edge_packaging_job_status.EdgePackagingJobStatus"
    ]
    """<p>The status of the edge packaging job.</p>"""
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the SageMaker Neo compilation job.</p>"""
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The version of the model.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the job was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the edge packaging job was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePackagingJobSummary) -> dict:
    out: dict = {}
    if "edge_packaging_job_arn" in value:
        out["EdgePackagingJobArn"] = value["edge_packaging_job_arn"]
    if "edge_packaging_job_name" in value:
        out["EdgePackagingJobName"] = value["edge_packaging_job_name"]
    if "edge_packaging_job_status" in value:
        import capo_sagemaker.types.edge_packaging_job_status

        out["EdgePackagingJobStatus"] = (
            capo_sagemaker.types.edge_packaging_job_status.serialize_aws_json_1_1(
                value["edge_packaging_job_status"]
            )
        )
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgePackagingJobSummary:
    out: EdgePackagingJobSummary = {}  # type: ignore[typeddict-item]
    if "EdgePackagingJobArn" in data:
        out["edge_packaging_job_arn"] = data["EdgePackagingJobArn"]
    if "EdgePackagingJobName" in data:
        out["edge_packaging_job_name"] = data["EdgePackagingJobName"]
    if "EdgePackagingJobStatus" in data:
        import capo_sagemaker.types.edge_packaging_job_status

        out["edge_packaging_job_status"] = (
            capo_sagemaker.types.edge_packaging_job_status.deserialize_aws_json_1_1(
                data["EdgePackagingJobStatus"]
            )
        )
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
