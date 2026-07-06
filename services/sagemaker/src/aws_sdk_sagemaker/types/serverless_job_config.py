"""Generated from Smithy shape ``com.amazonaws.sagemaker#ServerlessJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.accept_eula
    import aws_sdk_sagemaker.types.customization_technique
    import aws_sdk_sagemaker.types.evaluation_type
    import aws_sdk_sagemaker.types.evaluator_arn
    import aws_sdk_sagemaker.types.peft
    import aws_sdk_sagemaker.types.serverless_job_base_model_arn
    import aws_sdk_sagemaker.types.serverless_job_type


class ServerlessJobConfig(TypedDict, closed=True):
    base_model_arn: "aws_sdk_sagemaker.types.serverless_job_base_model_arn.ServerlessJobBaseModelArn"
    r"""<p> The base model Amazon Resource Name (ARN) in <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use.html\">SageMaker Public Hub</a>. SageMaker always selects the latest version of the provided model. </p>"""
    accept_eula: NotRequired["aws_sdk_sagemaker.types.accept_eula.AcceptEula"]
    r"""<p> Specifies agreement to the model end-user license agreement (EULA). The <code>AcceptEula</code> value must be explicitly defined as <code>True</code> in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula\">End-user license agreements</a> section for more details on accepting the EULA. </p>"""
    job_type: "aws_sdk_sagemaker.types.serverless_job_type.ServerlessJobType"
    """<p> The serverless training job type. </p>"""
    customization_technique: NotRequired[
        "aws_sdk_sagemaker.types.customization_technique.CustomizationTechnique"
    ]
    """<p> The model customization technique. </p>"""
    peft: NotRequired["aws_sdk_sagemaker.types.peft.Peft"]
    """<p> The parameter-efficient fine-tuning configuration. </p>"""
    evaluation_type: NotRequired[
        "aws_sdk_sagemaker.types.evaluation_type.EvaluationType"
    ]
    """<p> The evaluation job type. Required when serverless job type is <code>Evaluation</code>. </p>"""
    evaluator_arn: NotRequired["aws_sdk_sagemaker.types.evaluator_arn.EvaluatorArn"]
    """<p> The evaluator Amazon Resource Name (ARN) used as reward function or reward prompt. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerlessJobConfig) -> dict:
    out: dict = {}
    out["BaseModelArn"] = value["base_model_arn"]
    if "accept_eula" in value:
        out["AcceptEula"] = value["accept_eula"]
    import aws_sdk_sagemaker.types.serverless_job_type

    out["JobType"] = aws_sdk_sagemaker.types.serverless_job_type.serialize_aws_json_1_1(
        value["job_type"]
    )
    if "customization_technique" in value:
        import aws_sdk_sagemaker.types.customization_technique

        out["CustomizationTechnique"] = (
            aws_sdk_sagemaker.types.customization_technique.serialize_aws_json_1_1(
                value["customization_technique"]
            )
        )
    if "peft" in value:
        import aws_sdk_sagemaker.types.peft

        out["Peft"] = aws_sdk_sagemaker.types.peft.serialize_aws_json_1_1(value["peft"])
    if "evaluation_type" in value:
        import aws_sdk_sagemaker.types.evaluation_type

        out["EvaluationType"] = (
            aws_sdk_sagemaker.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation_type"]
            )
        )
    if "evaluator_arn" in value:
        out["EvaluatorArn"] = value["evaluator_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerlessJobConfig:
    out: ServerlessJobConfig = {}  # type: ignore[typeddict-item]
    if "BaseModelArn" in data:
        out["base_model_arn"] = data["BaseModelArn"]
    else:
        raise DeserializationError("ServerlessJobConfig.base_model_arn required")
    if "AcceptEula" in data:
        out["accept_eula"] = data["AcceptEula"]
    if "JobType" in data:
        import aws_sdk_sagemaker.types.serverless_job_type

        out["job_type"] = (
            aws_sdk_sagemaker.types.serverless_job_type.deserialize_aws_json_1_1(
                data["JobType"]
            )
        )
    else:
        raise DeserializationError("ServerlessJobConfig.job_type required")
    if "CustomizationTechnique" in data:
        import aws_sdk_sagemaker.types.customization_technique

        out["customization_technique"] = (
            aws_sdk_sagemaker.types.customization_technique.deserialize_aws_json_1_1(
                data["CustomizationTechnique"]
            )
        )
    if "Peft" in data:
        import aws_sdk_sagemaker.types.peft

        out["peft"] = aws_sdk_sagemaker.types.peft.deserialize_aws_json_1_1(
            data["Peft"]
        )
    if "EvaluationType" in data:
        import aws_sdk_sagemaker.types.evaluation_type

        out["evaluation_type"] = (
            aws_sdk_sagemaker.types.evaluation_type.deserialize_aws_json_1_1(
                data["EvaluationType"]
            )
        )
    if "EvaluatorArn" in data:
        out["evaluator_arn"] = data["EvaluatorArn"]
    return out
