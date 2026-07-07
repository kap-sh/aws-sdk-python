"""Generated from Smithy shape ``com.amazonaws.connect#Threshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.comparison
    import aws_sdk_connect.types.threshold_value


class Threshold(TypedDict, closed=True):
    comparison: NotRequired["aws_sdk_connect.types.comparison.Comparison"]
    r"""<p>The type of comparison. Only \"less than\" (LT) comparisons are supported.</p>"""
    threshold_value: NotRequired["aws_sdk_connect.types.threshold_value.ThresholdValue"]
    """<p>The threshold value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Threshold) -> dict:
    out: dict = {}
    if "comparison" in value:
        import aws_sdk_connect.types.comparison

        out["Comparison"] = aws_sdk_connect.types.comparison.serialize_json(
            value["comparison"]
        )
    if "threshold_value" in value:
        out["ThresholdValue"] = value["threshold_value"]
    return out


def deserialize_json(data: dict) -> Threshold:
    out: Threshold = {}  # type: ignore[typeddict-item]
    if "Comparison" in data:
        import aws_sdk_connect.types.comparison

        out["comparison"] = aws_sdk_connect.types.comparison.deserialize_json(
            data["Comparison"]
        )
    if "ThresholdValue" in data:
        out["threshold_value"] = data["ThresholdValue"]
    return out
