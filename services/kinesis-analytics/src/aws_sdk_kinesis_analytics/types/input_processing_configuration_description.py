"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputProcessingConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.input_lambda_processor_description


class InputProcessingConfigurationDescription(TypedDict):
    input_lambda_processor_description: NotRequired[
        "aws_sdk_kinesis_analytics.types.input_lambda_processor_description.InputLambdaProcessorDescription"
    ]
    r"""<p>Provides configuration information about the associated <a href=\"https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputLambdaProcessorDescription.html\">InputLambdaProcessorDescription</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputProcessingConfigurationDescription) -> dict:
    out: dict = {}
    if "input_lambda_processor_description" in value:
        import aws_sdk_kinesis_analytics.types.input_lambda_processor_description

        out["InputLambdaProcessorDescription"] = (
            aws_sdk_kinesis_analytics.types.input_lambda_processor_description.serialize_aws_json_1_1(
                value["input_lambda_processor_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputProcessingConfigurationDescription:
    out: InputProcessingConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "InputLambdaProcessorDescription" in data:
        import aws_sdk_kinesis_analytics.types.input_lambda_processor_description

        out["input_lambda_processor_description"] = (
            aws_sdk_kinesis_analytics.types.input_lambda_processor_description.deserialize_aws_json_1_1(
                data["InputLambdaProcessorDescription"]
            )
        )
    return out
