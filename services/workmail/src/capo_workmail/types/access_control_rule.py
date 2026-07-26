"""Generated from Smithy shape ``com.amazonaws.workmail#AccessControlRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_description
    import capo_workmail.types.access_control_rule_effect
    import capo_workmail.types.access_control_rule_name
    import capo_workmail.types.actions_list
    import capo_workmail.types.impersonation_role_id_list
    import capo_workmail.types.ip_range_list
    import capo_workmail.types.timestamp
    import capo_workmail.types.user_id_list


class AccessControlRule(TypedDict, closed=True):
    name: NotRequired[
        "capo_workmail.types.access_control_rule_name.AccessControlRuleName"
    ]
    """<p>The rule name.</p>"""
    effect: NotRequired[
        "capo_workmail.types.access_control_rule_effect.AccessControlRuleEffect"
    ]
    """<p>The rule effect.</p>"""
    description: NotRequired[
        "capo_workmail.types.access_control_rule_description.AccessControlRuleDescription"
    ]
    """<p>The rule description.</p>"""
    ip_ranges: NotRequired["capo_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to include in the rule.</p>"""
    not_ip_ranges: NotRequired["capo_workmail.types.ip_range_list.IpRangeList"]
    """<p>IPv4 CIDR ranges to exclude from the rule.</p>"""
    actions: NotRequired["capo_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to include in the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    not_actions: NotRequired["capo_workmail.types.actions_list.ActionsList"]
    """<p>Access protocol actions to exclude from the rule. Valid values include <code>ActiveSync</code>, <code>AutoDiscover</code>, <code>EWS</code>, <code>IMAP</code>, <code>SMTP</code>, <code>WindowsOutlook</code>, and <code>WebMail</code>.</p>"""
    user_ids: NotRequired["capo_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to include in the rule.</p>"""
    not_user_ids: NotRequired["capo_workmail.types.user_id_list.UserIdList"]
    """<p>User IDs to exclude from the rule.</p>"""
    date_created: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date that the rule was created.</p>"""
    date_modified: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date that the rule was modified.</p>"""
    impersonation_role_ids: NotRequired[
        "capo_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to include in the rule.</p>"""
    not_impersonation_role_ids: NotRequired[
        "capo_workmail.types.impersonation_role_id_list.ImpersonationRoleIdList"
    ]
    """<p>Impersonation role IDs to exclude from the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlRule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "effect" in value:
        import capo_workmail.types.access_control_rule_effect

        out["Effect"] = (
            capo_workmail.types.access_control_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "ip_ranges" in value:
        import capo_workmail.types.ip_range_list

        out["IpRanges"] = capo_workmail.types.ip_range_list.serialize_aws_json_1_1(
            value["ip_ranges"]
        )
    if "not_ip_ranges" in value:
        import capo_workmail.types.ip_range_list

        out["NotIpRanges"] = capo_workmail.types.ip_range_list.serialize_aws_json_1_1(
            value["not_ip_ranges"]
        )
    if "actions" in value:
        import capo_workmail.types.actions_list

        out["Actions"] = capo_workmail.types.actions_list.serialize_aws_json_1_1(
            value["actions"]
        )
    if "not_actions" in value:
        import capo_workmail.types.actions_list

        out["NotActions"] = capo_workmail.types.actions_list.serialize_aws_json_1_1(
            value["not_actions"]
        )
    if "user_ids" in value:
        import capo_workmail.types.user_id_list

        out["UserIds"] = capo_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["user_ids"]
        )
    if "not_user_ids" in value:
        import capo_workmail.types.user_id_list

        out["NotUserIds"] = capo_workmail.types.user_id_list.serialize_aws_json_1_1(
            value["not_user_ids"]
        )
    if "date_created" in value:
        import capo_workmail.types.timestamp

        out["DateCreated"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_created"]
        )
    if "date_modified" in value:
        import capo_workmail.types.timestamp

        out["DateModified"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["date_modified"]
        )
    if "impersonation_role_ids" in value:
        import capo_workmail.types.impersonation_role_id_list

        out["ImpersonationRoleIds"] = (
            capo_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["impersonation_role_ids"]
            )
        )
    if "not_impersonation_role_ids" in value:
        import capo_workmail.types.impersonation_role_id_list

        out["NotImpersonationRoleIds"] = (
            capo_workmail.types.impersonation_role_id_list.serialize_aws_json_1_1(
                value["not_impersonation_role_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessControlRule:
    out: AccessControlRule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Effect" in data:
        import capo_workmail.types.access_control_rule_effect

        out["effect"] = (
            capo_workmail.types.access_control_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "IpRanges" in data:
        import capo_workmail.types.ip_range_list

        out["ip_ranges"] = capo_workmail.types.ip_range_list.deserialize_aws_json_1_1(
            data["IpRanges"]
        )
    if "NotIpRanges" in data:
        import capo_workmail.types.ip_range_list

        out["not_ip_ranges"] = (
            capo_workmail.types.ip_range_list.deserialize_aws_json_1_1(
                data["NotIpRanges"]
            )
        )
    if "Actions" in data:
        import capo_workmail.types.actions_list

        out["actions"] = capo_workmail.types.actions_list.deserialize_aws_json_1_1(
            data["Actions"]
        )
    if "NotActions" in data:
        import capo_workmail.types.actions_list

        out["not_actions"] = capo_workmail.types.actions_list.deserialize_aws_json_1_1(
            data["NotActions"]
        )
    if "UserIds" in data:
        import capo_workmail.types.user_id_list

        out["user_ids"] = capo_workmail.types.user_id_list.deserialize_aws_json_1_1(
            data["UserIds"]
        )
    if "NotUserIds" in data:
        import capo_workmail.types.user_id_list

        out["not_user_ids"] = capo_workmail.types.user_id_list.deserialize_aws_json_1_1(
            data["NotUserIds"]
        )
    if "DateCreated" in data:
        import capo_workmail.types.timestamp

        out["date_created"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateCreated"]
        )
    if "DateModified" in data:
        import capo_workmail.types.timestamp

        out["date_modified"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DateModified"]
        )
    if "ImpersonationRoleIds" in data:
        import capo_workmail.types.impersonation_role_id_list

        out["impersonation_role_ids"] = (
            capo_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["ImpersonationRoleIds"]
            )
        )
    if "NotImpersonationRoleIds" in data:
        import capo_workmail.types.impersonation_role_id_list

        out["not_impersonation_role_ids"] = (
            capo_workmail.types.impersonation_role_id_list.deserialize_aws_json_1_1(
                data["NotImpersonationRoleIds"]
            )
        )
    return out
