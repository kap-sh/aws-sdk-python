"""Generated from Smithy shape ``com.amazonaws.sagemaker#CallbackStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.callback_token
    import aws_sdk_sagemaker.types.output_parameter_list
    import aws_sdk_sagemaker.types.string256


class CallbackStepMetadata(TypedDict, closed=True):
    callback_token: NotRequired["aws_sdk_sagemaker.types.callback_token.CallbackToken"]
    """<p>The pipeline generated token from the Amazon SQS queue.</p>"""
    sqs_queue_url: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The URL of the Amazon Simple Queue Service (Amazon SQS) queue used by the callback step.</p>"""
    output_parameters: NotRequired[
        "aws_sdk_sagemaker.types.output_parameter_list.OutputParameterList"
    ]
    """<p>A list of the output parameters of the callback step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallbackStepMetadata) -> dict:
    out: dict = {}
    if "callback_token" in value:
        out["CallbackToken"] = value["callback_token"]
    if "sqs_queue_url" in value:
        out["SqsQueueUrl"] = value["sqs_queue_url"]
    if "output_parameters" in value:
        import aws_sdk_sagemaker.types.output_parameter_list

        out["OutputParameters"] = (
            aws_sdk_sagemaker.types.output_parameter_list.serialize_aws_json_1_1(
                value["output_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CallbackStepMetadata:
    out: CallbackStepMetadata = {}  # type: ignore[typeddict-item]
    if "CallbackToken" in data:
        out["callback_token"] = data["CallbackToken"]
    if "SqsQueueUrl" in data:
        out["sqs_queue_url"] = data["SqsQueueUrl"]
    if "OutputParameters" in data:
        import aws_sdk_sagemaker.types.output_parameter_list

        out["output_parameters"] = (
            aws_sdk_sagemaker.types.output_parameter_list.deserialize_aws_json_1_1(
                data["OutputParameters"]
            )
        )
    return out
