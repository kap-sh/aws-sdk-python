"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidatorMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.metric_float


class ValidatorMetric(TypedDict, closed=True):
    validation_loss: NotRequired["capo_bedrock.types.metric_float.MetricFloat"]
    """<p>The validation loss associated with this validator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorMetric) -> dict:
    out: dict = {}
    if "validation_loss" in value:
        out["validationLoss"] = (
            "NaN"
            if value["validation_loss"] != value["validation_loss"]
            else "Infinity"
            if value["validation_loss"] == float("inf")
            else "-Infinity"
            if value["validation_loss"] == float("-inf")
            else value["validation_loss"]
        )
    return out


def deserialize_json(data: dict) -> ValidatorMetric:
    out: ValidatorMetric = {}  # type: ignore[typeddict-item]
    if data.get("validationLoss") is not None:
        out["validation_loss"] = float(data["validationLoss"])
    return out
