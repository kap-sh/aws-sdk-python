"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteNotifyMessageSpendLimitOverrideResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.monthly_limit


class DeleteNotifyMessageSpendLimitOverrideResult(TypedDict, closed=True):
    monthly_limit: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    ]
    """<p>The current monthly limit, in US dollars.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteNotifyMessageSpendLimitOverrideResult) -> dict:
    out: dict = {}
    if "monthly_limit" in value:
        out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteNotifyMessageSpendLimitOverrideResult:
    out: DeleteNotifyMessageSpendLimitOverrideResult = {}  # type: ignore[typeddict-item]
    if "MonthlyLimit" in data:
        out["monthly_limit"] = data["MonthlyLimit"]
    return out
