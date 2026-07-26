"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SpendLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.spend_limit_name


class SpendLimit(TypedDict, closed=True):
    name: "capo_pinpoint_sms_voice_v2.types.spend_limit_name.SpendLimitName"
    """<p>The name for the SpendLimit.</p>"""
    enforced_limit: "int"
    """<p>The maximum amount of money, in US dollars, that you want to be able to spend sending messages each month. This value has to be less than or equal to the amount in <code>MaxLimit</code>. To use this custom limit, <code>Overridden</code> must be set to true.</p>"""
    max_limit: "int"
    """<p> The maximum amount of money that you are able to spend to send messages each month, in US dollars.</p>"""
    overridden: "bool"
    """<p>When set to <code>True</code>, the value that has been specified in the <code>EnforcedLimit</code> is used to determine the maximum amount in US dollars that can be spent to send messages each month, in US dollars.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpendLimit) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["EnforcedLimit"] = value.get("enforced_limit", 0)
    out["MaxLimit"] = value.get("max_limit", 0)
    out["Overridden"] = value.get("overridden", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> SpendLimit:
    out: SpendLimit = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SpendLimit.name required")
    if "EnforcedLimit" in data:
        out["enforced_limit"] = data["EnforcedLimit"]
    else:
        out["enforced_limit"] = 0
    if "MaxLimit" in data:
        out["max_limit"] = data["MaxLimit"]
    else:
        out["max_limit"] = 0
    if "Overridden" in data:
        out["overridden"] = data["Overridden"]
    else:
        out["overridden"] = False
    return out
