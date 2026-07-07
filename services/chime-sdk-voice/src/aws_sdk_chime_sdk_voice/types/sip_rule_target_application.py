"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SipRuleTargetApplication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.sip_application_priority
    import aws_sdk_chime_sdk_voice.types.string


class SipRuleTargetApplication(TypedDict, closed=True):
    sip_media_application_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of a rule's target SIP media application.</p>"""
    priority: NotRequired[
        "aws_sdk_chime_sdk_voice.types.sip_application_priority.SipApplicationPriority"
    ]
    """<p>The priority setting of a rule's target SIP media application.</p>"""
    aws_region: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The AWS Region of a rule's target SIP media application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SipRuleTargetApplication) -> dict:
    out: dict = {}
    if "sip_media_application_id" in value:
        out["SipMediaApplicationId"] = value["sip_media_application_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_json(data: dict) -> SipRuleTargetApplication:
    out: SipRuleTargetApplication = {}  # type: ignore[typeddict-item]
    if "SipMediaApplicationId" in data:
        out["sip_media_application_id"] = data["SipMediaApplicationId"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
