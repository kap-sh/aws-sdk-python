"""Generated from Smithy shape ``com.amazonaws.connect#ThresholdV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.resource_arn_or_id
    import aws_sdk_connect.types.threshold_value


class ThresholdV2(TypedDict):
    comparison: NotRequired["aws_sdk_connect.types.resource_arn_or_id.ResourceArnOrId"]
    """<p>The type of comparison. Currently, \"less than\" (LT), \"less than equal\" (LTE), and \"greater than\" (GT) comparisons are supported.</p>"""
    threshold_value: NotRequired["aws_sdk_connect.types.threshold_value.ThresholdValue"]
    """<p>The threshold value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThresholdV2) -> dict:
    out: dict = {}
    if "comparison" in value:
        out["Comparison"] = value["comparison"]
    if "threshold_value" in value:
        out["ThresholdValue"] = value["threshold_value"]
    return out


def deserialize_json(data: dict) -> ThresholdV2:
    out: ThresholdV2 = {}  # type: ignore[typeddict-item]
    if "Comparison" in data:
        out["comparison"] = data["Comparison"]
    if "ThresholdValue" in data:
        out["threshold_value"] = data["ThresholdValue"]
    return out
