"""Generated from Smithy shape ``com.amazonaws.frauddetector#ATIMetricDataPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float


class ATIMetricDataPoint(TypedDict):
    cr: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The challenge rate. This indicates the percentage of login events that the model recommends to challenge such as one-time password, multi-factor authentication, and investigations. </p>"""
    adr: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The anomaly discovery rate. This metric quantifies the percentage of anomalies that can be detected by the model at the selected score threshold. A lower score threshold increases the percentage of anomalies captured by the model, but would also require challenging a larger percentage of login events, leading to a higher customer friction. </p>"""
    threshold: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The model's threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud. </p>"""
    atodr: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The account takeover discovery rate. This metric quantifies the percentage of account compromise events that can be detected by the model at the selected score threshold. This metric is only available if 50 or more entities with at-least one labeled account takeover event is present in the ingested dataset. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ATIMetricDataPoint) -> dict:
    out: dict = {}
    if "cr" in value:
        out["cr"] = value["cr"]
    if "adr" in value:
        out["adr"] = value["adr"]
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    if "atodr" in value:
        out["atodr"] = value["atodr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ATIMetricDataPoint:
    out: ATIMetricDataPoint = {}  # type: ignore[typeddict-item]
    if "cr" in data:
        out["cr"] = data["cr"]
    if "adr" in data:
        out["adr"] = data["adr"]
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    if "atodr" in data:
        out["atodr"] = data["atodr"]
    return out
