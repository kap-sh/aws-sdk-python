"""Generated from Smithy shape ``com.amazonaws.forecast#WindowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.evaluation_type
    import capo_forecast.types.integer
    import capo_forecast.types.metrics
    import capo_forecast.types.timestamp


class WindowSummary(TypedDict, closed=True):
    test_window_start: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that defines the start of the window.</p>"""
    test_window_end: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that defines the end of the window.</p>"""
    item_count: NotRequired["capo_forecast.types.integer.Integer"]
    """<p>The number of data points within the window.</p>"""
    evaluation_type: NotRequired["capo_forecast.types.evaluation_type.EvaluationType"]
    """<p>The type of evaluation.</p> <ul> <li> <p> <code>SUMMARY</code> - The average metrics across all windows.</p> </li> <li> <p> <code>COMPUTED</code> - The metrics for the specified window.</p> </li> </ul>"""
    metrics: NotRequired["capo_forecast.types.metrics.Metrics"]
    """<p>Provides metrics used to evaluate the performance of a predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowSummary) -> dict:
    out: dict = {}
    if "test_window_start" in value:
        import capo_forecast.types.timestamp

        out["TestWindowStart"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["test_window_start"]
        )
    if "test_window_end" in value:
        import capo_forecast.types.timestamp

        out["TestWindowEnd"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["test_window_end"]
        )
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "evaluation_type" in value:
        import capo_forecast.types.evaluation_type

        out["EvaluationType"] = (
            capo_forecast.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation_type"]
            )
        )
    if "metrics" in value:
        import capo_forecast.types.metrics

        out["Metrics"] = capo_forecast.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowSummary:
    out: WindowSummary = {}  # type: ignore[typeddict-item]
    if "TestWindowStart" in data:
        import capo_forecast.types.timestamp

        out["test_window_start"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["TestWindowStart"]
            )
        )
    if "TestWindowEnd" in data:
        import capo_forecast.types.timestamp

        out["test_window_end"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["TestWindowEnd"]
        )
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "EvaluationType" in data:
        import capo_forecast.types.evaluation_type

        out["evaluation_type"] = (
            capo_forecast.types.evaluation_type.deserialize_aws_json_1_1(
                data["EvaluationType"]
            )
        )
    if "Metrics" in data:
        import capo_forecast.types.metrics

        out["metrics"] = capo_forecast.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    return out
