"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#NotScaledReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.resource_capacity
    import aws_sdk_application_auto_scaling.types.xml_string


class NotScaledReason(TypedDict, closed=True):
    code: "aws_sdk_application_auto_scaling.types.xml_string.XmlString"
    """<p>A code that represents the reason for not scaling.</p> <p>Valid values:</p> <ul> <li> <p>AutoScalingAnticipatedFlapping</p> </li> <li> <p>TargetServicePutResourceAsUnscalable</p> </li> <li> <p>AlreadyAtMaxCapacity</p> </li> <li> <p>AlreadyAtMinCapacity</p> </li> <li> <p>AlreadyAtDesiredCapacity</p> </li> </ul>"""
    max_capacity: NotRequired[
        "aws_sdk_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The maximum capacity.</p>"""
    min_capacity: NotRequired[
        "aws_sdk_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The minimum capacity.</p>"""
    current_capacity: NotRequired[
        "aws_sdk_application_auto_scaling.types.resource_capacity.ResourceCapacity"
    ]
    """<p>The current capacity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotScaledReason) -> dict:
    out: dict = {}
    out["Code"] = value["code"]
    if "max_capacity" in value:
        out["MaxCapacity"] = value["max_capacity"]
    if "min_capacity" in value:
        out["MinCapacity"] = value["min_capacity"]
    if "current_capacity" in value:
        out["CurrentCapacity"] = value["current_capacity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotScaledReason:
    out: NotScaledReason = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("NotScaledReason.code required")
    if "MaxCapacity" in data:
        out["max_capacity"] = data["MaxCapacity"]
    if "MinCapacity" in data:
        out["min_capacity"] = data["MinCapacity"]
    if "CurrentCapacity" in data:
        out["current_capacity"] = data["CurrentCapacity"]
    return out
