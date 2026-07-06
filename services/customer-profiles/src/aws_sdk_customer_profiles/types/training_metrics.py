"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TrainingMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.metrics
    import aws_sdk_customer_profiles.types.timestamp


class TrainingMetrics(TypedDict, closed=True):
    time: NotRequired["aws_sdk_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp when these training metrics were recorded.</p>"""
    metrics: NotRequired["aws_sdk_customer_profiles.types.metrics.Metrics"]
    """<p>A collection of performance metrics and statistics from the training process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainingMetrics) -> dict:
    out: dict = {}
    if "time" in value:
        import aws_sdk_customer_profiles.types.timestamp

        out["Time"] = aws_sdk_customer_profiles.types.timestamp.serialize_json(
            value["time"]
        )
    if "metrics" in value:
        import aws_sdk_customer_profiles.types.metrics

        out["Metrics"] = aws_sdk_customer_profiles.types.metrics.serialize_json(
            value["metrics"]
        )
    return out


def deserialize_json(data: dict) -> TrainingMetrics:
    out: TrainingMetrics = {}  # type: ignore[typeddict-item]
    if "Time" in data:
        import aws_sdk_customer_profiles.types.timestamp

        out["time"] = aws_sdk_customer_profiles.types.timestamp.deserialize_json(
            data["Time"]
        )
    if "Metrics" in data:
        import aws_sdk_customer_profiles.types.metrics

        out["metrics"] = aws_sdk_customer_profiles.types.metrics.deserialize_json(
            data["Metrics"]
        )
    return out
