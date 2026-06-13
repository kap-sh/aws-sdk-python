"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountLimit``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_limit_name


class AccountLimit(TypedDict):
    name: "aws_sdk_pinpoint_sms_voice_v2.types.account_limit_name.AccountLimitName"
    """<p>The name of the attribute to apply the account limit to.</p>"""
    used: "int"
    """<p>The current amount that has been spent, in US dollars.</p>"""
    max: "int"
    """<p>The Amazon Web Services set limit for that resource type, in US dollars.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountLimit) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Used"] = value.get("used", 0)
    out["Max"] = value.get("max", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountLimit:
    out: AccountLimit = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AccountLimit.name required")
    if "Used" in data:
        out["used"] = data["Used"]
    else:
        out["used"] = 0
    if "Max" in data:
        out["max"] = data["Max"]
    else:
        out["max"] = 0
    return out
