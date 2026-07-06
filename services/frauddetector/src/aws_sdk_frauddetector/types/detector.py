"""Generated from Smithy shape ``com.amazonaws.frauddetector#Detector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.time


class Detector(TypedDict, closed=True):
    detector_id: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The detector ID.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The detector description.</p>"""
    event_type_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The name of the event type.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the detector was last updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the detector was created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The detector ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Detector) -> dict:
    out: dict = {}
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Detector:
    out: Detector = {}  # type: ignore[typeddict-item]
    if "detectorId" in data:
        out["detector_id"] = data["detectorId"]
    if "description" in data:
        out["description"] = data["description"]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
