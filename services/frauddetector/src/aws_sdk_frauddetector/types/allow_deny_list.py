"""Generated from Smithy shape ``com.amazonaws.frauddetector#AllowDenyList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.description
    import aws_sdk_frauddetector.types.fraud_detector_arn
    import aws_sdk_frauddetector.types.no_dash_identifier
    import aws_sdk_frauddetector.types.time
    import aws_sdk_frauddetector.types.variable_type


class AllowDenyList(TypedDict, closed=True):
    name: "aws_sdk_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list. </p>"""
    description: NotRequired["aws_sdk_frauddetector.types.description.description"]
    """<p> The description of the list. </p>"""
    variable_type: NotRequired["aws_sdk_frauddetector.types.variable_type.variableType"]
    """<p> The variable type of the list. </p>"""
    created_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p> The time the list was created. </p>"""
    updated_time: NotRequired["aws_sdk_frauddetector.types.time.time"]
    """<p> The time the list was last updated. </p>"""
    arn: NotRequired["aws_sdk_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p> The ARN of the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowDenyList) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "updated_time" in value:
        out["updatedTime"] = value["updated_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AllowDenyList:
    out: AllowDenyList = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AllowDenyList.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "variableType" in data:
        out["variable_type"] = data["variableType"]
    if "createdTime" in data:
        out["created_time"] = data["createdTime"]
    if "updatedTime" in data:
        out["updated_time"] = data["updatedTime"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
