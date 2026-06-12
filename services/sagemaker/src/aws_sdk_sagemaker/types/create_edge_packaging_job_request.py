"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEdgePackagingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edge_output_config
    import aws_sdk_sagemaker.types.edge_version
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateEdgePackagingJobRequest(TypedDict):
    edge_packaging_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the edge packaging job.</p>"""
    compilation_job_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the SageMaker Neo compilation job that will be used to locate model artifacts for packaging.</p>"""
    model_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["aws_sdk_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The version of the model.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to download and upload the model, and to contact SageMaker Neo.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.edge_output_config.EdgeOutputConfig"
    ]
    """<p>Provides information about the output location for the packaged model.</p>"""
    resource_key: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key to use when encrypting the EBS volume the edge packaging job runs on.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Creates tags for the packaging job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEdgePackagingJobRequest) -> dict:
    out: dict = {}
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
        import aws_sdk_sagemaker.types.edge_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.edge_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "resource_key" in value:
        out["ResourceKey"] = value["resource_key"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEdgePackagingJobRequest:
    out: CreateEdgePackagingJobRequest = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_sagemaker.types.edge_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.edge_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "ResourceKey" in data:
        out["resource_key"] = data["ResourceKey"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
