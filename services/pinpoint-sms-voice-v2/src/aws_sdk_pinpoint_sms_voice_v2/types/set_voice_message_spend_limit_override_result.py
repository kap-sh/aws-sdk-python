"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetVoiceMessageSpendLimitOverrideResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit


class SetVoiceMessageSpendLimitOverrideResult(TypedDict, closed=True):
    monthly_limit: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    ]
    """<p>The current monthly limit to enforce on sending voice messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetVoiceMessageSpendLimitOverrideResult) -> dict:
    out: dict = {}
    if "monthly_limit" in value:
        out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetVoiceMessageSpendLimitOverrideResult:
    out: SetVoiceMessageSpendLimitOverrideResult = {}  # type: ignore[typeddict-item]
    if "MonthlyLimit" in data:
        out["monthly_limit"] = data["MonthlyLimit"]
    return out
