"""Generated from Smithy shape ``com.amazonaws.acm#ThrottlingReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.coral_availability_throttled_resource
    import aws_sdk_acm.types.coral_availability_throttling_reason


class ThrottlingReason(TypedDict, closed=True):
    reason: NotRequired[
        "aws_sdk_acm.types.coral_availability_throttling_reason.CoralAvailabilityThrottlingReason"
    ]
    """<p>A description of why a request was throttled.</p>"""
    resource: NotRequired[
        "aws_sdk_acm.types.coral_availability_throttled_resource.CoralAvailabilityThrottledResource"
    ]
    """<p>The resource that causes the request to be throttled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingReason) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ThrottlingReason:
    out: ThrottlingReason = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "resource" in data:
        out["resource"] = data["resource"]
    return out
