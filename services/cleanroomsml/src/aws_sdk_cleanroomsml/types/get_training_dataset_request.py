"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainingDatasetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.training_dataset_arn


class GetTrainingDatasetRequest(TypedDict):
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainingDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrainingDatasetRequest:
    out: GetTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
