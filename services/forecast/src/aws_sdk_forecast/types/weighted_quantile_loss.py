"""Generated from Smithy shape ``com.amazonaws.forecast#WeightedQuantileLoss``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.double


class WeightedQuantileLoss(TypedDict, closed=True):
    quantile: NotRequired["aws_sdk_forecast.types.double.Double"]
    """<p>The quantile. Quantiles divide a probability distribution into regions of equal probability. For example, if the distribution was divided into 5 regions of equal probability, the quantiles would be 0.2, 0.4, 0.6, and 0.8.</p>"""
    loss_value: NotRequired["aws_sdk_forecast.types.double.Double"]
    """<p>The difference between the predicted value and the actual value over the quantile, weighted (normalized) by dividing by the sum over all quantiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WeightedQuantileLoss) -> dict:
    out: dict = {}
    if "quantile" in value:
        out["Quantile"] = value["quantile"]
    if "loss_value" in value:
        out["LossValue"] = value["loss_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WeightedQuantileLoss:
    out: WeightedQuantileLoss = {}  # type: ignore[typeddict-item]
    if "Quantile" in data:
        out["quantile"] = data["Quantile"]
    if "LossValue" in data:
        out["loss_value"] = data["LossValue"]
    return out
