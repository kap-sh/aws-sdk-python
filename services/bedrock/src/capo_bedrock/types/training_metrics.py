"""Generated from Smithy shape ``com.amazonaws.bedrock#TrainingMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.metric_float


class TrainingMetrics(TypedDict, closed=True):
    training_loss: NotRequired["capo_bedrock.types.metric_float.MetricFloat"]
    """<p>Loss metric associated with the custom job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingMetrics) -> dict:
    out: dict = {}
    if "training_loss" in value:
        out["trainingLoss"] = value["training_loss"]
    return out


def deserialize_json(data: dict) -> TrainingMetrics:
    out: TrainingMetrics = {}  # type: ignore[typeddict-item]
    if "trainingLoss" in data:
        out["training_loss"] = data["trainingLoss"]
    return out
