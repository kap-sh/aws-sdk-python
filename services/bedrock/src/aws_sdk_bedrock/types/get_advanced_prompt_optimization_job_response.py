"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAdvancedPromptOptimizationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_input_config
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_description
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_name
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status
    import aws_sdk_bedrock.types.advanced_prompt_optimization_output_config
    import aws_sdk_bedrock.types.error_message
    import aws_sdk_bedrock.types.kms_key_arn
    import aws_sdk_bedrock.types.model_configurations
    import aws_sdk_bedrock.types.timestamp


class GetAdvancedPromptOptimizationJobResponse(TypedDict, closed=True):
    job_arn: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_arn.AdvancedPromptOptimizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the advanced prompt optimization job.</p>"""
    job_name: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName"
    """<p>The name of the advanced prompt optimization job.</p>"""
    job_description: NotRequired[
        "aws_sdk_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
    ]
    """<p>The description of the advanced prompt optimization job.</p>"""
    job_status: "aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the advanced prompt optimization job.</p>"""
    input_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig"
    """<p>The input data configuration for the optimization job.</p>"""
    output_config: "aws_sdk_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig"
    """<p>The output data configuration for the optimization job.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_bedrock.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the output data.</p>"""
    creation_time: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the advanced prompt optimization job was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the advanced prompt optimization job was last modified.</p>"""
    failure_message: NotRequired["aws_sdk_bedrock.types.error_message.ErrorMessage"]
    """<p>If the job failed, a message describing the reason for the failure.</p>"""
    model_configurations: (
        "aws_sdk_bedrock.types.model_configurations.ModelConfigurations"
    )
    """<p>The model configurations used in the optimization job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdvancedPromptOptimizationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    if "job_description" in value:
        out["jobDescription"] = value["job_description"]
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    import aws_sdk_bedrock.types.advanced_prompt_optimization_input_config

    out["inputConfig"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_input_config.serialize_json(
            value["input_config"]
        )
    )
    import aws_sdk_bedrock.types.advanced_prompt_optimization_output_config

    out["outputConfig"] = (
        aws_sdk_bedrock.types.advanced_prompt_optimization_output_config.serialize_json(
            value["output_config"]
        )
    )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    import aws_sdk_bedrock.types.timestamp

    out["creationTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock.types.timestamp

        out["lastModifiedTime"] = aws_sdk_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    import aws_sdk_bedrock.types.model_configurations

    out["modelConfigurations"] = (
        aws_sdk_bedrock.types.model_configurations.serialize_json(
            value["model_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAdvancedPromptOptimizationJobResponse:
    out: GetAdvancedPromptOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.job_arn required"
        )
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.job_name required"
        )
    if "jobDescription" in data:
        out["job_description"] = data["jobDescription"]
    if "jobStatus" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_job_status

        out["job_status"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.job_status required"
        )
    if "inputConfig" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_input_config

        out["input_config"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_input_config.deserialize_json(
                data["inputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.input_config required"
        )
    if "outputConfig" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_output_config

        out["output_config"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.output_config required"
        )
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if "creationTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["creation_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.creation_time required"
        )
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock.types.timestamp

        out["last_modified_time"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    if "modelConfigurations" in data:
        import aws_sdk_bedrock.types.model_configurations

        out["model_configurations"] = (
            aws_sdk_bedrock.types.model_configurations.deserialize_json(
                data["modelConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "GetAdvancedPromptOptimizationJobResponse.model_configurations required"
        )
    return out
