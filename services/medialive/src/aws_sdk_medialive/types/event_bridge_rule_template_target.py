"""Generated from Smithy shape ``com.amazonaws.medialive#EventBridgeRuleTemplateTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string_min1_max2048_pattern_arn


class EventBridgeRuleTemplateTarget(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048_pattern_arn.__stringMin1Max2048PatternArn"
    ]
    """Target ARNs must be either an SNS topic or CloudWatch log group."""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeRuleTemplateTarget) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> EventBridgeRuleTemplateTarget:
    out: EventBridgeRuleTemplateTarget = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
