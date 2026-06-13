"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_attribute_name


class AccountAttribute(TypedDict):
    name: "aws_sdk_pinpoint_sms_voice_v2.types.account_attribute_name.AccountAttributeName"
    """<p>The name of the account attribute.</p>"""
    value: "str"
    """<p>The value associated with the account attribute name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountAttribute:
    out: AccountAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AccountAttribute.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("AccountAttribute.value required")
    return out
