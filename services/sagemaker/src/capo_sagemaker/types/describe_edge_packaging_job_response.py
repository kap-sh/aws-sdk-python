"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeEdgePackagingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_output_config
    import capo_sagemaker.types.edge_packaging_job_arn
    import capo_sagemaker.types.edge_packaging_job_status
    import capo_sagemaker.types.edge_preset_deployment_output
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.s3_uri
    import capo_sagemaker.types.string
    import capo_sagemaker.types.timestamp


class DescribeEdgePackagingJobResponse(TypedDict, closed=True):
    edge_packaging_job_arn: NotRequired[
        "capo_sagemaker.types.edge_packaging_job_arn.EdgePackagingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the edge packaging job.</p>"""
    edge_packaging_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the edge packaging job.</p>"""
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the SageMaker Neo compilation job that is used to locate model artifacts that are being packaged.</p>"""
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The version of the model.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to download and upload the model, and to contact Neo.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>The output configuration for the edge packaging job.</p>"""
    resource_key: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key to use when encrypting the EBS volume the job run on.</p>"""
    edge_packaging_job_status: NotRequired[
        "capo_sagemaker.types.edge_packaging_job_status.EdgePackagingJobStatus"
    ]
    """<p>The current status of the packaging job.</p>"""
    edge_packaging_job_status_message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>Returns a message describing the job status and error messages.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the packaging job was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of when the job was last updated.</p>"""
    model_artifact: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon Simple Storage (S3) URI where model artifacts ares stored.</p>"""
    model_signature: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The signature document of files in the model artifact.</p>"""
    preset_deployment_output: NotRequired[
        "capo_sagemaker.types.edge_preset_deployment_output.EdgePresetDeploymentOutput"
    ]
    """<p>The output of a SageMaker Edge Manager deployable resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEdgePackagingJobResponse) -> dict:
    out: dict = {}
    if "edge_packaging_job_arn" in value:
        out["EdgePackagingJobArn"] = value["edge_packaging_job_arn"]
    if "edge_packaging_job_name" in value:
        out["EdgePackagingJobName"] = value["edge_packaging_job_name"]
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "output_config" in value:
        import capo_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "resource_key" in value:
        out["ResourceKey"] = value["resource_key"]
    if "edge_packaging_job_status" in value:
        import capo_sagemaker.types.edge_packaging_job_status

        out["EdgePackagingJobStatus"] = (
            capo_sagemaker.types.edge_packaging_job_status.serialize_aws_json_1_1(
                value["edge_packaging_job_status"]
            )
        )
    if "edge_packaging_job_status_message" in value:
        out["EdgePackagingJobStatusMessage"] = value[
            "edge_packaging_job_status_message"
        ]
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
    if "model_artifact" in value:
        out["ModelArtifact"] = value["model_artifact"]
    if "model_signature" in value:
        out["ModelSignature"] = value["model_signature"]
    if "preset_deployment_output" in value:
        import capo_sagemaker.types.edge_preset_deployment_output

        out["PresetDeploymentOutput"] = (
            capo_sagemaker.types.edge_preset_deployment_output.serialize_aws_json_1_1(
                value["preset_deployment_output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEdgePackagingJobResponse:
    out: DescribeEdgePackagingJobResponse = {}  # type: ignore[typeddict-item]
    if "EdgePackagingJobArn" in data:
        out["edge_packaging_job_arn"] = data["EdgePackagingJobArn"]
    if "EdgePackagingJobName" in data:
        out["edge_packaging_job_name"] = data["EdgePackagingJobName"]
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "OutputConfig" in data:
        import capo_sagemaker.types.edge_output_config

        out["output_config"] = (
            capo_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "ResourceKey" in data:
        out["resource_key"] = data["ResourceKey"]
    if "EdgePackagingJobStatus" in data:
        import capo_sagemaker.types.edge_packaging_job_status

        out["edge_packaging_job_status"] = (
            capo_sagemaker.types.edge_packaging_job_status.deserialize_aws_json_1_1(
                data["EdgePackagingJobStatus"]
            )
        )
    if "EdgePackagingJobStatusMessage" in data:
        out["edge_packaging_job_status_message"] = data["EdgePackagingJobStatusMessage"]
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
    if "ModelArtifact" in data:
        out["model_artifact"] = data["ModelArtifact"]
    if "ModelSignature" in data:
        out["model_signature"] = data["ModelSignature"]
    if "PresetDeploymentOutput" in data:
        import capo_sagemaker.types.edge_preset_deployment_output

        out["preset_deployment_output"] = (
            capo_sagemaker.types.edge_preset_deployment_output.deserialize_aws_json_1_1(
                data["PresetDeploymentOutput"]
            )
        )
    return out
