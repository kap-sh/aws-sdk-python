"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetTextMessageSpendLimitOverrideRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit


class SetTextMessageSpendLimitOverrideRequest(TypedDict, closed=True):
    monthly_limit: "aws_sdk_pinpoint_sms_voice_v2.types.monthly_limit.MonthlyLimit"
    """<p>The new monthly limit to enforce on text messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetTextMessageSpendLimitOverrideRequest) -> dict:
    out: dict = {}
    out["MonthlyLimit"] = value["monthly_limit"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetTextMessageSpendLimitOverrideRequest:
    out: SetTextMessageSpendLimitOverrideRequest = {}  # type: ignore[typeddict-item]
    if "MonthlyLimit" in data:
        out["monthly_limit"] = data["MonthlyLimit"]
    else:
        raise DeserializationError(
            "SetTextMessageSpendLimitOverrideRequest.monthly_limit required"
        )
    return out
