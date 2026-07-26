"""Generated from Smithy shape ``com.amazonaws.frauddetector#Label``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time


class Label(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The label name.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The label description.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the label was last updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of when the event type was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The label ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Label) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Label:
    out: Label = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
