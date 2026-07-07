"""Generated from Smithy shape ``com.amazonaws.frauddetector#EntityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.time


class EntityType(TypedDict, closed=True):
    name: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The entity type name.</p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p>The entity type description.</p>"""
    last_updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the entity type was last updated.</p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p>Timestamp of when the entity type was created.</p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The entity type ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityType) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> EntityType:
    out: EntityType = {}  # type: ignore[typeddict-item]
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
