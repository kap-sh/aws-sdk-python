"""Generated from Smithy shape ``com.amazonaws.bedrock#GetCustomModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.customization_config
    import aws_sdk_bedrock.types.customization_type
    import aws_sdk_bedrock.types.error_message
    import aws_sdk_bedrock.types.job_name
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.model_customization_hyper_parameters
    import aws_sdk_bedrock.types.model_customization_job_arn
    import aws_sdk_bedrock.types.model_status
    import aws_sdk_bedrock.types.output_data_config
    import aws_sdk_bedrock.types.timestamp
    import aws_sdk_bedrock.types.training_data_config
    import aws_sdk_bedrock.types.training_metrics
    import aws_sdk_bedrock.types.validation_data_config
    import aws_sdk_bedrock.types.validation_metrics


class GetCustomModelResponse(TypedDict):
    model_arn: "aws_sdk_bedrock.types.model_arn.ModelArn"
    """<p>Amazon Resource Name (ARN) associated with this model.</p>"""
    model_name: "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    """<p>Model name associated with this model.</p>"""
    job_name: NotRequired["aws_sdk_bedrock.types.job_name.JobName"]
    """<p>Job name associated with this model.</p>"""
    job_arn: NotRequired[
        "aws_sdk_bedrock.types.model_customization_job_arn.ModelCustomizationJobArn"
    ]
    r"""<p>Job Amazon Resource Name (ARN) associated with this model. For models that you create with the <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModel.html\">CreateCustomModel</a> API operation, this is <code>NULL</code>.</p>"""
    base_model_arn: NotRequired["aws_sdk_bedrock.types.model_arn.ModelArn"]
    """<p>Amazon Resource Name (ARN) of the base model.</p>"""
    customization_type: NotRequired[
        "aws_sdk_bedrock.types.customization_type.CustomizationType"
    ]
    """<p>The type of model customization.</p>"""
    model_kms_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The custom model is encrypted at rest using this key.</p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
    ]
    r"""<p>Hyperparameter values associated with this model. For details on the format for different models, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html\">Custom model hyperparameters</a>.</p>"""
    training_data_config: NotRequired[
        "aws_sdk_bedrock.types.training_data_config.TrainingDataConfig"
    ]
    """<p>Contains information about the training dataset.</p>"""
    validation_data_config: NotRequired[
        "aws_sdk_bedrock.types.validation_data_config.ValidationDataConfig"
    ]
    """<p>Contains information about the validation dataset.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_bedrock.types.output_data_config.OutputDataConfig"
    ]
    """<p>Output data configuration associated with this custom model.</p>"""
    training_metrics: NotRequired[
        "aws_sdk_bedrock.types.training_metrics.TrainingMetrics"
    ]
    """<p>Contains training metrics from the job creation.</p>"""
    validation_metrics: NotRequired[
        "aws_sdk_bedrock.types.validation_metrics.ValidationMetrics"
    ]
    """<p>The validation metrics from the job creation.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>Creation time of the model.</p>"""
    customization_config: NotRequired[
        "aws_sdk_bedrock.types.customization_config.CustomizationConfig"
    ]
    """<p>The customization configuration for the custom model.</p>"""
    model_status: NotRequired["aws_sdk_bedrock.types.model_status.ModelStatus"]
    """<p>The current status of the custom model. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - The model is being created and validated.</p> </li> <li> <p> <code>Active</code> - The model has been successfully created and is ready for use.</p> </li> <li> <p> <code>Failed</code> - The model creation process failed. Check the <code>failureMessage</code> field for details.</p> </li> </ul>"""
    failure_message: NotRequired["aws_sdk_bedrock.types.error_message.ErrorMessage"]
    """<p>A failure message for any issues that occurred when creating the custom model. This is included for only a failed CreateCustomModel operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomModelResponse) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    out["modelName"] = value["model_name"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "base_model_arn" in value:
        out["baseModelArn"] = value["base_model_arn"]
    if "customization_type" in value:
        import aws_sdk_bedrock.types.customization_type

        out["customizationType"] = (
            aws_sdk_bedrock.types.customization_type.serialize_json(
                value["customization_type"]
            )
        )
    if "model_kms_key_arn" in value:
        out["modelKmsKeyArn"] = value["model_kms_key_arn"]
    if "hyper_parameters" in value:
        import aws_sdk_bedrock.types.model_customization_hyper_parameters

        out["hyperParameters"] = (
            aws_sdk_bedrock.types.model_customization_hyper_parameters.serialize_json(
                value["hyper_parameters"]
            )
        )
    if "training_data_config" in value:
        import aws_sdk_bedrock.types.training_data_config

        out["trainingDataConfig"] = (
            aws_sdk_bedrock.types.training_data_config.serialize_json(
                value["training_data_config"]
            )
        )
    if "validation_data_config" in value:
        import aws_sdk_bedrock.types.validation_data_config

        out["validationDataConfig"] = (
            aws_sdk_bedrock.types.validation_data_config.serialize_json(
                value["validation_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_bedrock.types.output_data_config

        out["outputDataConfig"] = (
            aws_sdk_bedrock.types.output_data_config.serialize_json(
                value["output_data_config"]
            )
        )
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
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "customization_config" in value:
        import aws_sdk_bedrock.types.customization_config

        out["customizationConfig"] = (
            aws_sdk_bedrock.types.customization_config.serialize_json(
                value["customization_config"]
            )
        )
    if "model_status" in value:
        import aws_sdk_bedrock.types.model_status

        out["modelStatus"] = aws_sdk_bedrock.types.model_status.serialize_json(
            value["model_status"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> GetCustomModelResponse:
    out: GetCustomModelResponse = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("GetCustomModelResponse.model_arn required")
    if "modelName" in data:
        out["model_name"] = data["modelName"]
    else:
        raise DeserializationError("GetCustomModelResponse.model_name required")
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "baseModelArn" in data:
        out["base_model_arn"] = data["baseModelArn"]
    if "customizationType" in data:
        import aws_sdk_bedrock.types.customization_type

        out["customization_type"] = (
            aws_sdk_bedrock.types.customization_type.deserialize_json(
                data["customizationType"]
            )
        )
    if "modelKmsKeyArn" in data:
        out["model_kms_key_arn"] = data["modelKmsKeyArn"]
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
    if "validationDataConfig" in data:
        import aws_sdk_bedrock.types.validation_data_config

        out["validation_data_config"] = (
            aws_sdk_bedrock.types.validation_data_config.deserialize_json(
                data["validationDataConfig"]
            )
        )
    if "outputDataConfig" in data:
        import aws_sdk_bedrock.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_bedrock.types.output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
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
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetCustomModelResponse.creation_time required")
    if "customizationConfig" in data:
        import aws_sdk_bedrock.types.customization_config

        out["customization_config"] = (
            aws_sdk_bedrock.types.customization_config.deserialize_json(
                data["customizationConfig"]
            )
        )
    if "modelStatus" in data:
        import aws_sdk_bedrock.types.model_status

        out["model_status"] = aws_sdk_bedrock.types.model_status.deserialize_json(
            data["modelStatus"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
