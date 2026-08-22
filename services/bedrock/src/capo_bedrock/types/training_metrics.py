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
        out["trainingLoss"] = (
            "NaN"
            if value["training_loss"] != value["training_loss"]
            else "Infinity"
            if value["training_loss"] == float("inf")
            else "-Infinity"
            if value["training_loss"] == float("-inf")
            else value["training_loss"]
        )
    return out


def deserialize_json(data: dict) -> TrainingMetrics:
    out: TrainingMetrics = {}  # type: ignore[typeddict-item]
    if data.get("trainingLoss") is not None:
        out["training_loss"] = float(data["trainingLoss"])
    return out
