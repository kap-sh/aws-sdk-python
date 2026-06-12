"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteMobileDeviceAccessRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_rule_id
    import aws_sdk_workmail.types.organization_id


class DeleteMobileDeviceAccessRuleRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which the rule will be deleted.</p>"""
    mobile_device_access_rule_id: (
        "aws_sdk_workmail.types.mobile_device_access_rule_id.MobileDeviceAccessRuleId"
    )
    """<p>The identifier of the rule to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMobileDeviceAccessRuleRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["MobileDeviceAccessRuleId"] = value["mobile_device_access_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMobileDeviceAccessRuleRequest:
    out: DeleteMobileDeviceAccessRuleRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "DeleteMobileDeviceAccessRuleRequest.organization_id required"
        )
    if "MobileDeviceAccessRuleId" in data:
        out["mobile_device_access_rule_id"] = data["MobileDeviceAccessRuleId"]
    else:
        raise DeserializationError(
            "DeleteMobileDeviceAccessRuleRequest.mobile_device_access_rule_id required"
        )
    return out
