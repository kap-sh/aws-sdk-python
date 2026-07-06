"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputProcessingConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update


class InputProcessingConfigurationUpdate(TypedDict, closed=True):
    input_lambda_processor_update: "aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update.InputLambdaProcessorUpdate"
    """<p>Provides update information for an <a>InputLambdaProcessor</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputProcessingConfigurationUpdate) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update

    out["InputLambdaProcessorUpdate"] = (
        aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update.serialize_aws_json_1_1(
            value["input_lambda_processor_update"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputProcessingConfigurationUpdate:
    out: InputProcessingConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "InputLambdaProcessorUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update

        out["input_lambda_processor_update"] = (
            aws_sdk_kinesis_analytics_v2.types.input_lambda_processor_update.deserialize_aws_json_1_1(
                data["InputLambdaProcessorUpdate"]
            )
        )
    else:
        raise DeserializationError(
            "InputProcessingConfigurationUpdate.input_lambda_processor_update required"
        )
    return out
