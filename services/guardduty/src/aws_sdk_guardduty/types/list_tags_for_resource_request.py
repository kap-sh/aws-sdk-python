"""Generated from Smithy shape ``com.amazonaws.guardduty#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.guard_duty_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_guardduty.types.guard_duty_arn.GuardDutyArn"
    """<p>The Amazon Resource Name (ARN) for the given GuardDuty resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
