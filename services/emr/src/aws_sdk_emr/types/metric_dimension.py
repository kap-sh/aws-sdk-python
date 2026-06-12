"""Generated from Smithy shape ``com.amazonaws.emr#MetricDimension``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string


class MetricDimension(TypedDict):
    key: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The dimension name.</p>"""
    value: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The dimension value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimension) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
