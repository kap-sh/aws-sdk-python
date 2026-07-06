"""Generated from Smithy shape ``com.amazonaws.workmail#PutAccessControlRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_control_rule_description
    import aws_sdk_workmail.types.access_control_rule_effect
    import aws_sdk_workmail.types.access_control_rule_name
    import aws_sdk_workmail.types.actions_list
    import aws_sdk_workmail.types.impersonation_role_id_list
    import aws_sdk_workmail.types.ip_range_list
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.user_id_list


class PutAccessControlRuleRequest(TypedDict, closed=True):
    name: "aws_sdk_workmail.types.access_control_rule_name.AccessControlRuleName"
    """<p>The rule name.</p>"""
    effect: "aws_sdk_workmail.types.access_control_rule_effect.AccessControlRuleEffect"
    """<p>The rule effect.</p>"""
    description: "aws_sdk_workmail.types.access_control_rule_description.AccessControlRuleDescription"
    """<p>The rule description.</p>"""
    ip_ranges: NotRequired["aws_sdk_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to include in the rule.</p>"""
    not_ip_ranges: NotRequired["aws_sdk_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to exclude from the rule.</p>"""
    actions: NotRequired["aws_sdk_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to include in the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    not_actions: NotRequired["aws_sdk_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to exclude from the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    user_ids: NotRequired["aws_sdk_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to include in the rule.</p>"""
    not_user_ids: NotRequired["aws_sdk_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to exclude from the rule.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization.</p>"""
    impersonation_role_ids: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to include in the rule.</p>"""
    not_impersonation_role_ids: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to exclude from the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccessControlRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_workmail.types.access_control_rule_effect

    out["Effect"] = (
        aws_sdk_workmail.types.access_control_rule_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    out["Description"] = value["description"]
    if "ip_ranges" in value:
        import aws_sdk_workmail.types.ip_range_list

        out["IpRanges"] = aws_sdk_workmail.types.ip_range_list.serialize_aws_json_1_1(
            value["ip_ranges"]
        )
    if "not_ip_ranges" in value:
        import aws_sdk_workmail.types.ip_range_list

        out["NotIpRanges"] = (
            aws_sdk_workmail.types.ip_range_list.serialize_aws_json_1_1(
                value["not_ip_ranges"]
            )
        )
    if "actions" in value:
        import aws_sdk_workmail.types.actions_list

        out["Actions"] = aws_sdk_workmail.types.actions_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "not_actions" in value:
        import aws_sdk_workmail.types.actions_list

        out["NotActions"] = aws_sdk_workmail.types.actions_list.serialize_aws_json_1_1(
            value["not_actions"]
        )
    if "user_ids" in value:
        import aws_sdk_workmail.types.user_id_list

        out["UserIds"] = aws_sdk_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["user_ids"]
        )
    if "not_user_ids" in value:
        import aws_sdk_workmail.types.user_id_list

        out["NotUserIds"] = aws_sdk_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["not_user_ids"]
        )
    out["OrganizationId"] = value["organization_id"]
    if "impersonation_role_ids" in value:
        import aws_sdk_workmail.types.impersonation_role_id_list

        out["ImpersonationRoleIds"] = (
            aws_sdk_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["impersonation_role_ids"]
            )
        )
    if "not_impersonation_role_ids" in value:
        import aws_sdk_workmail.types.impersonation_role_id_list

        out["NotImpersonationRoleIds"] = (
            aws_sdk_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["not_impersonation_role_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccessControlRuleRequest:
    out: PutAccessControlRuleRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutAccessControlRuleRequest.name required")
    if "Effect" in data:
        import aws_sdk_workmail.types.access_control_rule_effect

        out["effect"] = (
            aws_sdk_workmail.types.access_control_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        raise DeserializationError("PutAccessControlRuleRequest.effect required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("PutAccessControlRuleRequest.description required")
    if "IpRanges" in data:
        import aws_sdk_workmail.types.ip_range_list

        out["ip_ranges"] = (
            aws_sdk_workmail.types.ip_range_list.deserialize_aws_json_1_1(
                data["IpRanges"]
            )
        )
    if "NotIpRanges" in data:
        import aws_sdk_workmail.types.ip_range_list

        out["not_ip_ranges"] = (
            aws_sdk_workmail.types.ip_range_list.deserialize_aws_json_1_1(
                data["NotIpRanges"]
            )
        )
    if "Actions" in data:
        import aws_sdk_workmail.types.actions_list

        out["actions"] = aws_sdk_workmail.types.actions_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if "NotActions" in data:
        import aws_sdk_workmail.types.actions_list

        out["not_actions"] = (
            aws_sdk_workmail.types.actions_list.deserialize_aws_json_1_1(
                data["NotActions"]
            )
        )
    if "UserIds" in data:
        import aws_sdk_workmail.types.user_id_list

        out["user_ids"] = aws_sdk_workmail.types.user_id_list.deserialize_aws_json_1_1(
            data["UserIds"]
        )
    if "NotUserIds" in data:
        import aws_sdk_workmail.types.user_id_list

        out["not_user_ids"] = (
            aws_sdk_workmail.types.user_id_list.deserialize_aws_json_1_1(
                data["NotUserIds"]
            )
        )
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "PutAccessControlRuleRequest.organization_id required"
        )
    if "ImpersonationRoleIds" in data:
        import aws_sdk_workmail.types.impersonation_role_id_list

        out["impersonation_role_ids"] = (
            aws_sdk_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["ImpersonationRoleIds"]
            )
        )
    if "NotImpersonationRoleIds" in data:
        import aws_sdk_workmail.types.impersonation_role_id_list

        out["not_impersonation_role_ids"] = (
            aws_sdk_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["NotImpersonationRoleIds"]
            )
        )
    return out
