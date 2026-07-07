"""Generated from Smithy shape ``com.amazonaws.workmail#GetAccessControlEffectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_control_rule_action
    import aws_sdk_workmail.types.impersonation_role_id
    import aws_sdk_workmail.types.ip_address
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.work_mail_identifier


class GetAccessControlEffectRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization.</p>"""
    ip_address: "aws_sdk_workmail.types.ip_address.IpAddress"
    """<p>The IPv4 address.</p>"""
    action: "aws_sdk_workmail.types.access_control_rule_action.AccessControlRuleAction"
    """<p>The access protocol action. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    user_id: NotRequired[
        "aws_sdk_workmail.types.work_mail_identifier.WorkMailIdentifier"
    ]
    """<p>The user ID.</p>"""
    impersonation_role_id: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_id.ImpersonationRoleId"
    ]
    """<p>The impersonation role ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessControlEffectRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["IpAddress"] = value["ip_address"]
    out["Action"] = value["action"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "impersonation_role_id" in value:
        out["ImpersonationRoleId"] = value["impersonation_role_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessControlEffectRequest:
    out: GetAccessControlEffectRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "GetAccessControlEffectRequest.organization_id required"
        )
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    else:
        raise DeserializationError("GetAccessControlEffectRequest.ip_address required")
    if "Action" in data:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("GetAccessControlEffectRequest.action required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "ImpersonationRoleId" in data:
        out["impersonation_role_id"] = data["ImpersonationRoleId"]
    return out
