"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.account_id
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.firewall_rule_group_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rfc3339_time_string
    import capo_route53resolver.types.share_status
    import capo_route53resolver.types.status_message
    import capo_route53resolver.types.unsigned


class FirewallRuleGroup(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the rule group. </p>"""
    arn: NotRequired["capo_route53resolver.types.arn.Arn"]
    """<p>The ARN (Amazon Resource Name) of the rule group.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the rule group.</p>"""
    rule_count: NotRequired["capo_route53resolver.types.unsigned.Unsigned"]
    """<p>The number of rules in the rule group.</p>"""
    status: NotRequired[
        "capo_route53resolver.types.firewall_rule_group_status.FirewallRuleGroupStatus"
    ]
    """<p>The status of the domain list. </p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the rule group, if available.</p>"""
    owner_id: NotRequired["capo_route53resolver.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the account that created the rule group. When a rule group is shared with your account, this is the account that has shared the rule group with you. </p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    share_status: NotRequired["capo_route53resolver.types.share_status.ShareStatus"]
    """<p>Whether the rule group is shared with other Amazon Web Services accounts, or was shared with the current account by another Amazon Web Services account. Sharing is configured through Resource Access Manager (RAM).</p>"""
    creation_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the rule group was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the rule group was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_count" in value:
        out["RuleCount"] = value["rule_count"]
    if "status" in value:
        import capo_route53resolver.types.firewall_rule_group_status

        out["Status"] = (
            capo_route53resolver.types.firewall_rule_group_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "share_status" in value:
        import capo_route53resolver.types.share_status

        out["ShareStatus"] = (
            capo_route53resolver.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleGroup:
    out: FirewallRuleGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RuleCount" in data:
        out["rule_count"] = data["RuleCount"]
    if "Status" in data:
        import capo_route53resolver.types.firewall_rule_group_status

        out["status"] = (
            capo_route53resolver.types.firewall_rule_group_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "ShareStatus" in data:
        import capo_route53resolver.types.share_status

        out["share_status"] = (
            capo_route53resolver.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    return out
