"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetVoiceMessageSpendLimitOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.monthly_limit


class SetVoiceMessageSpendLimitOverrideRequest(TypedDict, closed=True):
    monthly_limit: "capo_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    """<p>The new monthly limit to enforce on voice messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetVoiceMessageSpendLimitOverrideRequest) -> dict:
    out: dict = {}
    out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetVoiceMessageSpendLimitOverrideRequest:
    out: SetVoiceMessageSpendLimitOverrideRequest = {}  # type: ignore[typeddict-item]
    if "MonthlyLimit" in data:
        out["monthly_limit"] = data["MonthlyLimit"]
    else:
        raise DeserializationError(
            "SetVoiceMessageSpendLimitOverrideRequest.monthly_limit required"
        )
    return out
