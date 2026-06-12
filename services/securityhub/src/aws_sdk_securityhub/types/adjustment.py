"""Generated from Smithy shape ``com.amazonaws.securityhub#Adjustment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class Adjustment(TypedDict):
    metric: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The metric to adjust.</p>"""
    reason: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Adjustment) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> Adjustment:
    out: Adjustment = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
