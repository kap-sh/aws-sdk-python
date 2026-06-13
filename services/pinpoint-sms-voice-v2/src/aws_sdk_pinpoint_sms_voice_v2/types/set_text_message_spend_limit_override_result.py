"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetTextMessageSpendLimitOverrideResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit


class SetTextMessageSpendLimitOverrideResult(TypedDict):
    monthly_limit: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    ]
    """<p>The current monthly limit to enforce on sending text messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetTextMessageSpendLimitOverrideResult) -> dict:
    out: dict = {}
    if "monthly_limit" in value:
        out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetTextMessageSpendLimitOverrideResult:
    out: SetTextMessageSpendLimitOverrideResult = {}  # type: ignore[typeddict-item]
    if "MonthlyLimit" in data:
        out["monthly_limit"] = data["MonthlyLimit"]
    return out
