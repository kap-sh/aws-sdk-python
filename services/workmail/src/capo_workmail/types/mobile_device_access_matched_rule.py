"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessMatchedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.mobile_device_access_rule_id
    import capo_workmail.types.mobile_device_access_rule_name


class MobileDeviceAccessMatchedRule(TypedDict, closed=True):
    mobile_device_access_rule_id: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    ]
    """<p>Identifier of the rule that a simulated user matches.</p>"""
    name: NotRequired[
        "capo_workmail.types.mobile_device_access_rule_name.MobileDeviceAccessRuleName"
    ]
    """<p>Name of a rule that a simulated user matches.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessMatchedRule) -> dict:
    out: dict = {}
    if "mobile_device_access_rule_id" in value:
        out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MobileDeviceAccessMatchedRule:
    out: MobileDeviceAccessMatchedRule = {}  # type: ignore[typeddict-item]
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
