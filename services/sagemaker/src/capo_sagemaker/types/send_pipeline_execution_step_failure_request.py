"""Generated from Smithy shape ``com.amazonaws.sagemaker#SendPipelineExecutionStepFailureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.callback_token
    import capo_sagemaker.types.idempotency_token
    import capo_sagemaker.types.string256


class SendPipelineExecutionStepFailureRequest(TypedDict, closed=True):
    callback_token: NotRequired["capo_sagemaker.types.callback_token.CallbackToken"]
    """<p>The pipeline generated token from the Amazon SQS queue.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>A message describing why the step failed.</p>"""
    client_request_token: NotRequired[
        "capo_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendPipelineExecutionStepFailureRequest) -> dict:
    out: dict = {}
    if "callback_token" in value:
        out["CallbackToken"] = value["callback_token"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendPipelineExecutionStepFailureRequest:
    out: SendPipelineExecutionStepFailureRequest = {}  # type: ignore[typeddict-item]
    if "CallbackToken" in data:
        out["callback_token"] = data["CallbackToken"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
