"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CancelTrainedModelInferenceJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_arn
    import aws_sdk_cleanroomsml.types.uuid


class CancelTrainedModelInferenceJobRequest(TypedDict):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the trained model inference job that you want to cancel.</p>"""
    trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job that you want to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTrainedModelInferenceJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelTrainedModelInferenceJobRequest:
    out: CancelTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
    return out
