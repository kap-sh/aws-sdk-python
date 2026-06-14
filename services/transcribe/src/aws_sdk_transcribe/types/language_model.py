"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.base_model_name
    import aws_sdk_transcribe.types.boolean
    import aws_sdk_transcribe.types.clm_language_code
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.input_data_config
    import aws_sdk_transcribe.types.model_name
    import aws_sdk_transcribe.types.model_status


class LanguageModel(TypedDict):
    model_name: NotRequired["aws_sdk_transcribe.types.model_name.ModelName"]
    """<p>A unique name, chosen by you, for your custom language model.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account.</p>"""
    create_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom language model was created.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    last_modified_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified custom language model was last modified.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe.types.clm_language_code.CLMLanguageCode"
    ]
    r"""<p>The language code used to create your custom language model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.</p> <p>For a list of supported languages and their associated language codes, refer to the <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\">Supported languages</a> table. Note that US English (<code>en-US</code>) is the only language supported with Amazon Transcribe Medical.</p>"""
    base_model_name: NotRequired[
        "aws_sdk_transcribe.types.base_model_name.BaseModelName"
    ]
    """<p>The Amazon Transcribe standard language model, or base model, used to create your custom language model.</p>"""
    model_status: NotRequired["aws_sdk_transcribe.types.model_status.ModelStatus"]
    """<p>The status of the specified custom language model. When the status displays as <code>COMPLETED</code> the model is ready for use.</p>"""
    upgrade_availability: NotRequired["aws_sdk_transcribe.types.boolean.Boolean"]
    """<p>Shows if a more current base model is available for use with the specified custom language model.</p> <p>If <code>false</code>, your custom language model is using the most up-to-date base model.</p> <p>If <code>true</code>, there is a newer base model available than the one your language model is using.</p> <p>Note that to update a base model, you must recreate the custom language model using the new base model. Base model upgrades for existing custom language models are not supported.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>ModelStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the custom language model request failed. See also: <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_transcribe.types.input_data_config.InputDataConfig"
    ]
    """<p>The Amazon S3 location of the input files used to train and tune your custom language model, in addition to the data access role ARN (Amazon Resource Name) that has permissions to access these data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageModel) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "create_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CreateTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["LastModifiedTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
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
    if "model_status" in value:
        import aws_sdk_transcribe.types.model_status

        out["ModelStatus"] = (
            aws_sdk_transcribe.types.model_status.serialize_aws_json_1_1(
                value["model_status"]
            )
        )
    if "upgrade_availability" in value:
        out["UpgradeAvailability"] = value["upgrade_availability"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "input_data_config" in value:
        import aws_sdk_transcribe.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_transcribe.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LanguageModel:
    out: LanguageModel = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "CreateTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["create_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CreateTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["last_modified_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
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
    if "ModelStatus" in data:
        import aws_sdk_transcribe.types.model_status

        out["model_status"] = (
            aws_sdk_transcribe.types.model_status.deserialize_aws_json_1_1(
                data["ModelStatus"]
            )
        )
    if "UpgradeAvailability" in data:
        out["upgrade_availability"] = data["UpgradeAvailability"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "InputDataConfig" in data:
        import aws_sdk_transcribe.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_transcribe.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    return out
