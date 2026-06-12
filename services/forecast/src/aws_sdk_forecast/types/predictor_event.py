"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.detail
    import aws_sdk_forecast.types.timestamp


class PredictorEvent(TypedDict):
    detail: NotRequired["aws_sdk_forecast.types.detail.Detail"]
    """<p>The type of event. For example, <code>Retrain</code>. A retraining event denotes the timepoint when a predictor was retrained. Any monitor results from before the <code>Datetime</code> are from the previous predictor. Any new metrics are for the newly retrained predictor.</p>"""
    datetime: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp for when the event occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorEvent) -> dict:
    out: dict = {}
    if "detail" in value:
        out["Detail"] = value["detail"]
    if "datetime" in value:
        import aws_sdk_forecast.types.timestamp

        out["Datetime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["datetime"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorEvent:
    out: PredictorEvent = {}  # type: ignore[typeddict-item]
    if "Detail" in data:
        out["detail"] = data["Detail"]
    if "Datetime" in data:
        import aws_sdk_forecast.types.timestamp

        out["datetime"] = aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["Datetime"]
        )
    return out
