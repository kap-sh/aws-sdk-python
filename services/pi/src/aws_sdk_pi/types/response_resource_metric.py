"""Generated from Smithy shape ``com.amazonaws.pi#ResponseResourceMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pi.types.description
    import aws_sdk_pi.types.string


class ResponseResourceMetric(TypedDict, closed=True):
    metric: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The full name of the metric.</p>"""
    description: NotRequired["aws_sdk_pi.types.description.Description"]
    """<p>The description of the metric.</p>"""
    unit: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The unit of the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseResourceMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "description" in value:
        out["Description"] = value["description"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseResourceMetric:
    out: ResponseResourceMetric = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
