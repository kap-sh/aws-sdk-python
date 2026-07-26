"""Generated from Smithy shape ``com.amazonaws.forecast#Metrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.error_metrics
    import capo_forecast.types.weighted_quantile_losses


class Metrics(TypedDict, closed=True):
    rmse: NotRequired["capo_forecast.types.double.Double"]
    """<p>The root-mean-square error (RMSE).</p>"""
    weighted_quantile_losses: NotRequired[
        "capo_forecast.types.weighted_quantile_losses.WeightedQuantileLosses"
    ]
    """<p>An array of weighted quantile losses. Quantiles divide a probability distribution into regions of equal probability. The distribution in this case is the loss function.</p>"""
    error_metrics: NotRequired["capo_forecast.types.error_metrics.ErrorMetrics"]
    """<p> Provides detailed error metrics for each forecast type. Metrics include root-mean square-error (RMSE), mean absolute percentage error (MAPE), mean absolute scaled error (MASE), and weighted average percentage error (WAPE). </p>"""
    average_weighted_quantile_loss: NotRequired["capo_forecast.types.double.Double"]
    """<p>The average value of all weighted quantile losses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Metrics) -> dict:
    out: dict = {}
    if "rmse" in value:
        out["RMSE"] = value["rmse"]
    if "weighted_quantile_losses" in value:
        import capo_forecast.types.weighted_quantile_losses

        out["WeightedQuantileLosses"] = (
            capo_forecast.types.weighted_quantile_losses.serialize_aws_json_1_1(
                value["weighted_quantile_losses"]
            )
        )
    if "error_metrics" in value:
        import capo_forecast.types.error_metrics

        out["ErrorMetrics"] = capo_forecast.types.error_metrics.serialize_aws_json_1_1(
            value["error_metrics"]
        )
    if "average_weighted_quantile_loss" in value:
        out["AverageWeightedQuantileLoss"] = value["average_weighted_quantile_loss"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Metrics:
    out: Metrics = {}  # type: ignore[typeddict-item]
    if "RMSE" in data:
        out["rmse"] = data["RMSE"]
    if "WeightedQuantileLosses" in data:
        import capo_forecast.types.weighted_quantile_losses

        out["weighted_quantile_losses"] = (
            capo_forecast.types.weighted_quantile_losses.deserialize_aws_json_1_1(
                data["WeightedQuantileLosses"]
            )
        )
    if "ErrorMetrics" in data:
        import capo_forecast.types.error_metrics

        out["error_metrics"] = (
            capo_forecast.types.error_metrics.deserialize_aws_json_1_1(
                data["ErrorMetrics"]
            )
        )
    if "AverageWeightedQuantileLoss" in data:
        out["average_weighted_quantile_loss"] = data["AverageWeightedQuantileLoss"]
    return out
