"""Generated from Smithy shape ``com.amazonaws.workmail#CreateMobileDeviceAccessRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_rule_id


class CreateMobileDeviceAccessRuleResponse(TypedDict):
    mobile_device_access_rule_id: NotRequired[
        "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    ]
    """<p>The identifier for the newly created mobile device access rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMobileDeviceAccessRuleResponse) -> dict:
    out: dict = {}
    if "mobile_device_access_rule_id" in value:
        out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMobileDeviceAccessRuleResponse:
    out: CreateMobileDeviceAccessRuleResponse = {}  # type: ignore[typeddict-item]
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    return out
