"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceExperimentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_metadata
    import aws_sdk_sagemaker.types.inference_experiment_arn
    import aws_sdk_sagemaker.types.inference_experiment_data_storage_config
    import aws_sdk_sagemaker.types.inference_experiment_description
    import aws_sdk_sagemaker.types.inference_experiment_name
    import aws_sdk_sagemaker.types.inference_experiment_schedule
    import aws_sdk_sagemaker.types.inference_experiment_status
    import aws_sdk_sagemaker.types.inference_experiment_status_reason
    import aws_sdk_sagemaker.types.inference_experiment_type
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.model_variant_config_summary_list
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.shadow_mode_config
    import aws_sdk_sagemaker.types.timestamp


class DescribeInferenceExperimentResponse(TypedDict):
    arn: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_arn.InferenceExperimentArn"
    ]
    """<p>The ARN of the inference experiment being described.</p>"""
    name: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment.</p>"""
    type: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    """<p>The type of the inference experiment.</p>"""
    schedule: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_schedule.InferenceExperimentSchedule"
    ]
    """<p>The duration for which the inference experiment ran or will run.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status.InferenceExperimentStatus"
    ]
    r"""<p> The status of the inference experiment. The following are the possible statuses for an inference experiment: </p> <ul> <li> <p> <code>Creating</code> - Amazon SageMaker is creating your experiment. </p> </li> <li> <p> <code>Created</code> - Amazon SageMaker has finished the creation of your experiment and will begin the experiment at the scheduled time. </p> </li> <li> <p> <code>Updating</code> - When you make changes to your experiment, your experiment shows as updating. </p> </li> <li> <p> <code>Starting</code> - Amazon SageMaker is beginning your experiment. </p> </li> <li> <p> <code>Running</code> - Your experiment is in progress. </p> </li> <li> <p> <code>Stopping</code> - Amazon SageMaker is stopping your experiment. </p> </li> <li> <p> <code>Completed</code> - Your experiment has completed. </p> </li> <li> <p> <code>Cancelled</code> - When you conclude your experiment early using the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html\">StopInferenceExperiment</a> API, or if any operation fails with an unexpected error, it shows as cancelled. </p> </li> </ul>"""
    status_reason: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_status_reason.InferenceExperimentStatusReason"
    ]
    r"""<p> The error message or client-specified <code>Reason</code> from the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopInferenceExperiment.html\">StopInferenceExperiment</a> API, that explains the status of the inference experiment. </p>"""
    description: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_description.InferenceExperimentDescription"
    ]
    """<p>The description of the inference experiment.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which you created the inference experiment.</p>"""
    completion_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p> The timestamp at which the inference experiment was completed. </p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp at which you last modified the inference experiment.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p> The ARN of the IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment. </p>"""
    endpoint_metadata: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_metadata.EndpointMetadata"
    ]
    """<p>The metadata of the endpoint on which the inference experiment ran.</p>"""
    model_variants: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_config_summary_list.ModelVariantConfigSummaryList"
    ]
    """<p> An array of <code>ModelVariantConfigSummary</code> objects. There is one for each variant in the inference experiment. Each <code>ModelVariantConfigSummary</code> object in the array describes the infrastructure configuration for deploying the corresponding variant. </p>"""
    data_storage_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_data_storage_config.InferenceExperimentDataStorageConfig"
    ]
    """<p>The Amazon S3 location and configuration for storing inference request and response data.</p>"""
    shadow_mode_config: NotRequired[
        "aws_sdk_sagemaker.types.shadow_mode_config.ShadowModeConfig"
    ]
    """<p> The configuration of <code>ShadowMode</code> inference experiment type, which shows the production variant that takes all the inference requests, and the shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also shows the percentage of requests that Amazon SageMaker replicates. </p>"""
    kms_key: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    r"""<p> The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html\">CreateInferenceExperiment</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceExperimentResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["Type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "schedule" in value:
        import aws_sdk_sagemaker.types.inference_experiment_schedule

        out["Schedule"] = (
            aws_sdk_sagemaker.types.inference_experiment_schedule.serialize_aws_json_1_1(
                value["schedule"]
            )
        )
    if "status" in value:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["Status"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CompletionTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "endpoint_metadata" in value:
        import aws_sdk_sagemaker.types.endpoint_metadata

        out["EndpointMetadata"] = (
            aws_sdk_sagemaker.types.endpoint_metadata.serialize_aws_json_1_1(
                value["endpoint_metadata"]
            )
        )
    if "model_variants" in value:
        import aws_sdk_sagemaker.types.model_variant_config_summary_list

        out["ModelVariants"] = (
            aws_sdk_sagemaker.types.model_variant_config_summary_list.serialize_aws_json_1_1(
                value["model_variants"]
            )
        )
    if "data_storage_config" in value:
        import aws_sdk_sagemaker.types.inference_experiment_data_storage_config

        out["DataStorageConfig"] = (
            aws_sdk_sagemaker.types.inference_experiment_data_storage_config.serialize_aws_json_1_1(
                value["data_storage_config"]
            )
        )
    if "shadow_mode_config" in value:
        import aws_sdk_sagemaker.types.shadow_mode_config

        out["ShadowModeConfig"] = (
            aws_sdk_sagemaker.types.shadow_mode_config.serialize_aws_json_1_1(
                value["shadow_mode_config"]
            )
        )
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceExperimentResponse:
    out: DescribeInferenceExperimentResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.inference_experiment_type

        out["type"] = (
            aws_sdk_sagemaker.types.inference_experiment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Schedule" in data:
        import aws_sdk_sagemaker.types.inference_experiment_schedule

        out["schedule"] = (
            aws_sdk_sagemaker.types.inference_experiment_schedule.deserialize_aws_json_1_1(
                data["Schedule"]
            )
        )
    if "Status" in data:
        import aws_sdk_sagemaker.types.inference_experiment_status

        out["status"] = (
            aws_sdk_sagemaker.types.inference_experiment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        out["status_reason"] = data["StatusReason"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["completion_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "EndpointMetadata" in data:
        import aws_sdk_sagemaker.types.endpoint_metadata

        out["endpoint_metadata"] = (
            aws_sdk_sagemaker.types.endpoint_metadata.deserialize_aws_json_1_1(
                data["EndpointMetadata"]
            )
        )
    if "ModelVariants" in data:
        import aws_sdk_sagemaker.types.model_variant_config_summary_list

        out["model_variants"] = (
            aws_sdk_sagemaker.types.model_variant_config_summary_list.deserialize_aws_json_1_1(
                data["ModelVariants"]
            )
        )
    if "DataStorageConfig" in data:
        import aws_sdk_sagemaker.types.inference_experiment_data_storage_config

        out["data_storage_config"] = (
            aws_sdk_sagemaker.types.inference_experiment_data_storage_config.deserialize_aws_json_1_1(
                data["DataStorageConfig"]
            )
        )
    if "ShadowModeConfig" in data:
        import aws_sdk_sagemaker.types.shadow_mode_config

        out["shadow_mode_config"] = (
            aws_sdk_sagemaker.types.shadow_mode_config.deserialize_aws_json_1_1(
                data["ShadowModeConfig"]
            )
        )
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    return out
