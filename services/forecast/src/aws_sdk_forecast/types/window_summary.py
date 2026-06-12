"""Generated from Smithy shape ``com.amazonaws.forecast#WindowSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.evaluation_type
    import aws_sdk_forecast.types.integer
    import aws_sdk_forecast.types.metrics
    import aws_sdk_forecast.types.timestamp


class WindowSummary(TypedDict):
    test_window_start: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that defines the start of the window.</p>"""
    test_window_end: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp that defines the end of the window.</p>"""
    item_count: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of data points within the window.</p>"""
    evaluation_type: NotRequired[
        "aws_sdk_forecast.types.evaluation_type.EvaluationType"
    ]
    """<p>The type of evaluation.</p> <ul> <li> <p> <code>SUMMARY</code> - The average metrics across all windows.</p> </li> <li> <p> <code>COMPUTED</code> - The metrics for the specified window.</p> </li> </ul>"""
    metrics: NotRequired["aws_sdk_forecast.types.metrics.Metrics"]
    """<p>Provides metrics used to evaluate the performance of a predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowSummary) -> dict:
    out: dict = {}
    if "test_window_start" in value:
        import aws_sdk_forecast.types.timestamp

        out["TestWindowStart"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["test_window_start"]
            )
        )
    if "test_window_end" in value:
        import aws_sdk_forecast.types.timestamp

        out["TestWindowEnd"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["test_window_end"]
        )
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "evaluation_type" in value:
        import aws_sdk_forecast.types.evaluation_type

        out["EvaluationType"] = (
            aws_sdk_forecast.types.evaluation_type.serialize_aws_json_1_1(
                value["evaluation_type"]
            )
        )
    if "metrics" in value:
        import aws_sdk_forecast.types.metrics

        out["Metrics"] = aws_sdk_forecast.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WindowSummary:
    out: WindowSummary = {}  # type: ignore[typeddict-item]
    if "TestWindowStart" in data:
        import aws_sdk_forecast.types.timestamp

        out["test_window_start"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["TestWindowStart"]
            )
        )
    if "TestWindowEnd" in data:
        import aws_sdk_forecast.types.timestamp

        out["test_window_end"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["TestWindowEnd"]
            )
        )
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "EvaluationType" in data:
        import aws_sdk_forecast.types.evaluation_type

        out["evaluation_type"] = (
            aws_sdk_forecast.types.evaluation_type.deserialize_aws_json_1_1(
                data["EvaluationType"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_forecast.types.metrics

        out["metrics"] = aws_sdk_forecast.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    return out
