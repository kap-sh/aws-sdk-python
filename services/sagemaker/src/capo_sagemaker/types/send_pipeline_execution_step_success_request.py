"""Generated from Smithy shape ``com.amazonaws.sagemaker#SendPipelineExecutionStepSuccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.callback_token
    import capo_sagemaker.types.idempotency_token
    import capo_sagemaker.types.output_parameter_list


class SendPipelineExecutionStepSuccessRequest(TypedDict, closed=True):
    callback_token: NotRequired["capo_sagemaker.types.callback_token.CallbackToken"]
    """<p>The pipeline generated token from the Amazon SQS queue.</p>"""
    output_parameters: NotRequired[
        "capo_sagemaker.types.output_parameter_list.OutputParameterList"
    ]
    """<p>A list of the output parameters of the callback step.</p>"""
    client_request_token: NotRequired[
        "capo_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendPipelineExecutionStepSuccessRequest) -> dict:
    out: dict = {}
    if "callback_token" in value:
        out["CallbackToken"] = value["callback_token"]
    if "output_parameters" in value:
        import capo_sagemaker.types.output_parameter_list

        out["OutputParameters"] = (
            capo_sagemaker.types.output_parameter_list.serialize_aws_json_1_1(
                value["output_parameters"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendPipelineExecutionStepSuccessRequest:
    out: SendPipelineExecutionStepSuccessRequest = {}  # type: ignore[typeddict-item]
    if "CallbackToken" in data:
        out["callback_token"] = data["CallbackToken"]
    if "OutputParameters" in data:
        import capo_sagemaker.types.output_parameter_list

        out["output_parameters"] = (
            capo_sagemaker.types.output_parameter_list.deserialize_aws_json_1_1(
                data["OutputParameters"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
