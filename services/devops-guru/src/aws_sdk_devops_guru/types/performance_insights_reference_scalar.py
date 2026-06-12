"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsReferenceScalar``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.performance_insights_value_double


class PerformanceInsightsReferenceScalar(TypedDict):
    value: NotRequired[
        "aws_sdk_devops_guru.types.performance_insights_value_double.PerformanceInsightsValueDouble"
    ]
    """<p>The reference value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsReferenceScalar) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PerformanceInsightsReferenceScalar:
    out: PerformanceInsightsReferenceScalar = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
