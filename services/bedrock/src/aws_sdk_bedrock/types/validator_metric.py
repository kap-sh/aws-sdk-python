"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidatorMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.metric_float


class ValidatorMetric(TypedDict, closed=True):
    validation_loss: NotRequired["aws_sdk_bedrock.types.metric_float.MetricFloat"]
    """<p>The validation loss associated with this validator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorMetric) -> dict:
    out: dict = {}
    if "validation_loss" in value:
        out["validationLoss"] = value["validation_loss"]
    return out


def deserialize_json(data: dict) -> ValidatorMetric:
    out: ValidatorMetric = {}  # type: ignore[typeddict-item]
    if "validationLoss" in data:
        out["validation_loss"] = data["validationLoss"]
    return out
