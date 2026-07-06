"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteTrainingDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.training_dataset_arn


class DeleteTrainingDatasetRequest(TypedDict, closed=True):
    training_dataset_arn: (
        "aws_sdk_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn"
    )
    """<p>The Amazon Resource Name (ARN) of the training dataset that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrainingDatasetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrainingDatasetRequest:
    out: DeleteTrainingDatasetRequest = {}  # type: ignore[typeddict-item]
    return out
