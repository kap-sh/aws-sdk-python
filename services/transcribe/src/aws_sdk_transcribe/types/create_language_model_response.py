"""Generated from Smithy shape ``com.amazonaws.transcribe#CreateLanguageModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.base_model_name
    import aws_sdk_transcribe.types.clm_language_code
    import aws_sdk_transcribe.types.input_data_config
    import aws_sdk_transcribe.types.model_name
    import aws_sdk_transcribe.types.model_status


class CreateLanguageModelResponse(TypedDict):
    language_code: NotRequired[
        "aws_sdk_transcribe.types.clm_language_code.CLMLanguageCode"
    ]
    """<p>The language code you selected for your custom language model.</p>"""
    base_model_name: NotRequired[
        "aws_sdk_transcribe.types.base_model_name.BaseModelName"
    ]
    """<p>The Amazon Transcribe standard language model, or base model, you specified when creating your custom language model.</p>"""
    model_name: NotRequired["aws_sdk_transcribe.types.model_name.ModelName"]
    """<p>The name of your custom language model.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_transcribe.types.input_data_config.InputDataConfig"
    ]
    """<p>Lists your data access role ARN (Amazon Resource Name) and the Amazon S3 locations you provided for your training (<code>S3Uri</code>) and tuning (<code>TuningDataS3Uri</code>) data.</p>"""
    model_status: NotRequired["aws_sdk_transcribe.types.model_status.ModelStatus"]
    """<p>The status of your custom language model. When the status displays as <code>COMPLETED</code>, your model is ready to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLanguageModelResponse) -> dict:
    out: dict = {}
    if "language_code" in value:
        import aws_sdk_transcribe.types.clm_language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.clm_language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "base_model_name" in value:
        import aws_sdk_transcribe.types.base_model_name

        out["BaseModelName"] = (
            aws_sdk_transcribe.types.base_model_name.serialize_aws_json_1_1(
                value["base_model_name"]
            )
        )
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "input_data_config" in value:
        import aws_sdk_transcribe.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_transcribe.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "model_status" in value:
        import aws_sdk_transcribe.types.model_status

        out["ModelStatus"] = (
            aws_sdk_transcribe.types.model_status.serialize_aws_json_1_1(
                value["model_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLanguageModelResponse:
    out: CreateLanguageModelResponse = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.clm_language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.clm_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "BaseModelName" in data:
        import aws_sdk_transcribe.types.base_model_name

        out["base_model_name"] = (
            aws_sdk_transcribe.types.base_model_name.deserialize_aws_json_1_1(
                data["BaseModelName"]
            )
        )
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "InputDataConfig" in data:
        import aws_sdk_transcribe.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_transcribe.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "ModelStatus" in data:
        import aws_sdk_transcribe.types.model_status

        out["model_status"] = (
            aws_sdk_transcribe.types.model_status.deserialize_aws_json_1_1(
                data["ModelStatus"]
            )
        )
    return out
