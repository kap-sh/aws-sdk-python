"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelCustomizationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_arn
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.customization_config
    import aws_sdk_bedrock.types.customization_type
    import aws_sdk_bedrock.types.error_message
    import aws_sdk_bedrock.types.foundation_model_arn
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.job_name
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.model_customization_hyper_parameters
    import aws_sdk_bedrock.types.model_customization_job_arn
    import aws_sdk_bedrock.types.model_customization_job_status
    import aws_sdk_bedrock.types.output_data_config
    import aws_sdk_bedrock.types.role_arn
    import aws_sdk_bedrock.types.status_details
    import aws_sdk_bedrock.types.timestamp
    import aws_sdk_bedrock.types.training_data_config
    import aws_sdk_bedrock.types.training_metrics
    import aws_sdk_bedrock.types.validation_data_config
    import aws_sdk_bedrock.types.validation_metrics
    import aws_sdk_bedrock.types.vpc_config


class GetModelCustomizationJobResponse(TypedDict):
    job_arn: (
        "aws_sdk_bedrock.types.model_customization_job_arn.ModelCustomizationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the customization job.</p>"""
    job_name: "aws_sdk_bedrock.types.job_name.JobName"
    """<p>The name of the customization job.</p>"""
    output_model_name: "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    """<p>The name of the output model.</p>"""
    output_model_arn: NotRequired[
        "aws_sdk_bedrock.types.custom_model_arn.CustomModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the output model.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>The token that you specified in the <code>CreateCustomizationJob</code> request.</p>"""
    role_arn: "aws_sdk_bedrock.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""
    status: NotRequired[
        "aws_sdk_bedrock.types.model_customization_job_status.ModelCustomizationJobStatus"
    ]
    """<p>The status of the job. A successful job transitions from in-progress to completed when the output model is ready to use. If the job failed, the failure message contains information about why the job failed.</p>"""
    status_details: NotRequired["aws_sdk_bedrock.types.status_details.StatusDetails"]
    """<p>For a Distillation job, the details about the statuses of the sub-tasks of the customization job. </p>"""
    failure_message: NotRequired["aws_sdk_bedrock.types.error_message.ErrorMessage"]
    """<p>Information about why the job failed.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>Time that the resource was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the resource was last modified.</p>"""
    end_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Time that the resource transitioned to terminal state.</p>"""
    base_model_arn: "aws_sdk_bedrock.types.foundation_model_arn.FoundationModelArn"
    """<p>Amazon Resource Name (ARN) of the base model.</p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
    ]
    """<p>The hyperparameter values for the job. For details on the format for different models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html\">Custom model hyperparameters</a>.</p>"""
    training_data_config: (
        "aws_sdk_bedrock.types.training_data_config.TrainingDataConfig"
    )
    """<p>Contains information about the training dataset.</p>"""
    validation_data_config: (
        "aws_sdk_bedrock.types.validation_data_config.ValidationDataConfig"
    )
    """<p>Contains information about the validation dataset.</p>"""
    output_data_config: "aws_sdk_bedrock.types.output_data_config.OutputDataConfig"
    """<p>Output data configuration </p>"""
    customization_type: NotRequired[
        "aws_sdk_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>The type of model customization.</p>"""
    output_model_kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The custom model is encrypted at rest using this key.</p>"""
    training_metrics: NotRequired[
        "aws_sdk_bedrock.types.training_metrics.TrainingMetrics"
    ]
    """<p>Contains training metrics from the job creation.</p>"""
    validation_metrics: NotRequired[
        "aws_sdk_bedrock.types.validation_metrics.ValidationMetrics"
    ]
    """<p>The loss metric for each validator that you provided in the createjob request.</p>"""
    vpc_config: NotRequired["aws_sdk_bedrock.types.vpc_config.VpcConfig"]
    """<p>VPC configuration for the custom model job.</p>"""
    customization_config: NotRequired[
        "aws_sdk_bedrock.types.customization_config.CustomizationConfig"
    ]
    """<p>The customization configuration for the model customization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelCustomizationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    out["outputModelName"] = value["output_model_name"]
    if "output_model_arn" in value:
        out["outputModelArn"] = value["output_model_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["roleArn"] = value["role_arn"]
    if "status" in value:
        import aws_sdk_bedrock.types.model_customization_job_status

        out["status"] = (
            aws_sdk_bedrock.types.model_customization_job_status.serialize_json(
                value["status"]
            )
        )
    if "status_details" in value:
        import aws_sdk_bedrock.types.status_details

        out["statusDetails"] = aws_sdk_bedrock.types.status_details.serialize_json(
            value["status_details"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastModifiedTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "end_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["endTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["end_time"]
        )
    out["baseModelArn"] = value["base_model_arn"]
    if "hyper_parameters" in value:
        import aws_sdk_bedrock.types.model_customization_hyper_parameters

        out["hyperParameters"] = (
            aws_sdk_bedrock.types.model_customization_hyper_parameters.serialize_json(
                value["hyper_parameters"]
            )
        )
    import aws_sdk_bedrock.types.training_data_config

    out["trainingDataConfig"] = (
        aws_sdk_bedrock.types.training_data_config.serialize_json(
            value["training_data_config"]
        )
    )
    import aws_sdk_bedrock.types.validation_data_config

    out["validationDataConfig"] = (
        aws_sdk_bedrock.types.validation_data_config.serialize_json(
            value["validation_data_config"]
        )
    )
    import aws_sdk_bedrock.types.output_data_config

    out["outputDataConfig"] = aws_sdk_bedrock.types.output_data_config.serialize_json(
        value["output_data_config"]
    )
    if "customization_type" in value:
        import aws_sdk_bedrock.types.customization_type

        out["customizationType"] = (
            aws_sdk_bedrock.types.customization_type.serialize_json(
                value["customization_type"]
            )
        )
    if "output_model_kms_key_arn" in value:
        out["outputModelKmsKeyArn"] = value["output_model_kms_key_arn"]
    if "training_metrics" in value:
        import aws_sdk_bedrock.types.training_metrics

        out["trainingMetrics"] = aws_sdk_bedrock.types.training_metrics.serialize_json(
            value["training_metrics"]
        )
    if "validation_metrics" in value:
        import aws_sdk_bedrock.types.validation_metrics

        out["validationMetrics"] = (
            aws_sdk_bedrock.types.validation_metrics.serialize_json(
                value["validation_metrics"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_bedrock.types.vpc_config

        out["vpcConfig"] = aws_sdk_bedrock.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "customization_config" in value:
        import aws_sdk_bedrock.types.customization_config

        out["customizationConfig"] = (
            aws_sdk_bedrock.types.customization_config.serialize_json(
                value["customization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetModelCustomizationJobResponse:
    out: GetModelCustomizationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.job_arn required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.job_name required")
    if "outputModelName" in data:
        out["output_model_name"] = data["outputModelName"]
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.output_model_name required"
        )
    if "outputModelArn" in data:
        out["output_model_arn"] = data["outputModelArn"]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetModelCustomizationJobResponse.role_arn required")
    if "status" in data:
        import aws_sdk_bedrock.types.model_customization_job_status

        out["status"] = (
            aws_sdk_bedrock.types.model_customization_job_status.deserialize_json(
                data["status"]
            )
        )
    if "statusDetails" in data:
        import aws_sdk_bedrock.types.status_details

        out["status_details"] = aws_sdk_bedrock.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.creation_time required"
        )
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_modified_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if "endTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["end_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["endTime"]
        )
    if "baseModelArn" in data:
        out["base_model_arn"] = data["baseModelArn"]
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.base_model_arn required"
        )
    if "hyperParameters" in data:
        import aws_sdk_bedrock.types.model_customization_hyper_parameters

        out["hyper_parameters"] = (
            aws_sdk_bedrock.types.model_customization_hyper_parameters.deserialize_json(
                data["hyperParameters"]
            )
        )
    if "trainingDataConfig" in data:
        import aws_sdk_bedrock.types.training_data_config

        out["training_data_config"] = (
            aws_sdk_bedrock.types.training_data_config.deserialize_json(
                data["trainingDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.training_data_config required"
        )
    if "validationDataConfig" in data:
        import aws_sdk_bedrock.types.validation_data_config

        out["validation_data_config"] = (
            aws_sdk_bedrock.types.validation_data_config.deserialize_json(
                data["validationDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.validation_data_config required"
        )
    if "outputDataConfig" in data:
        import aws_sdk_bedrock.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_bedrock.types.output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetModelCustomizationJobResponse.output_data_config required"
        )
    if "customizationType" in data:
        import aws_sdk_bedrock.types.customization_type

        out["customization_type"] = (
            aws_sdk_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    if "outputModelKmsKeyArn" in data:
        out["output_model_kms_key_arn"] = data["outputModelKmsKeyArn"]
    if "trainingMetrics" in data:
        import aws_sdk_bedrock.types.training_metrics

        out["training_metrics"] = (
            aws_sdk_bedrock.types.training_metrics.deserialize_json(
                data["trainingMetrics"]
            )
        )
    if "validationMetrics" in data:
        import aws_sdk_bedrock.types.validation_metrics

        out["validation_metrics"] = (
            aws_sdk_bedrock.types.validation_metrics.deserialize_json(
                data["validationMetrics"]
            )
        )
    if "vpcConfig" in data:
        import aws_sdk_bedrock.types.vpc_config

        out["vpc_config"] = aws_sdk_bedrock.types.vpc_config.deserialize_json(
            data["vpcConfig"]
        )
    if "customizationConfig" in data:
        import aws_sdk_bedrock.types.customization_config

        out["customization_config"] = (
            aws_sdk_bedrock.types.customization_config.deserialize_json(
                data["customizationConfig"]
            )
        )
    return out
