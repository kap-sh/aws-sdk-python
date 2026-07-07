"""Generated from Smithy shape ``com.amazonaws.frauddetector#OFIMetricDataPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.float


class OFIMetricDataPoint(TypedDict, closed=True):
    fpr: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The false positive rate. This is the percentage of total legitimate events that are incorrectly predicted as fraud. </p>"""
    precision: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The percentage of fraud events correctly predicted as fraudulent as compared to all events predicted as fraudulent. </p>"""
    tpr: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The true positive rate. This is the percentage of total fraud the model detects. Also known as capture rate. </p>"""
    threshold: NotRequired["aws_sdk_frauddetector.types.float.float"]
    """<p> The model threshold that specifies an acceptable fraud capture rate. For example, a threshold of 500 means any model score 500 or above is labeled as fraud. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OFIMetricDataPoint) -> dict:
    out: dict = {}
    if "fpr" in value:
        out["fpr"] = value["fpr"]
    if "precision" in value:
        out["precision"] = value["precision"]
    if "tpr" in value:
        out["tpr"] = value["tpr"]
    if "threshold" in value:
        out["threshold"] = value["threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OFIMetricDataPoint:
    out: OFIMetricDataPoint = {}  # type: ignore[typeddict-item]
    if "fpr" in data:
        out["fpr"] = data["fpr"]
    if "precision" in data:
        out["precision"] = data["precision"]
    if "tpr" in data:
        out["tpr"] = data["tpr"]
    if "threshold" in data:
        out["threshold"] = data["threshold"]
    return out
