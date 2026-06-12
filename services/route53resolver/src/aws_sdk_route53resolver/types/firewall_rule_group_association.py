"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRuleGroupAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.firewall_rule_group_association_status
    import aws_sdk_route53resolver.types.mutation_protection_status
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.priority
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.rfc3339_time_string
    import aws_sdk_route53resolver.types.service_principle
    import aws_sdk_route53resolver.types.status_message


class FirewallRuleGroupAssociation(TypedDict):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The identifier for the association.</p>"""
    arn: NotRequired["aws_sdk_route53resolver.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the firewall rule group association.</p>"""
    firewall_rule_group_id: NotRequired[
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the firewall rule group. </p>"""
    vpc_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The unique identifier of the VPC that is associated with the rule group. </p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The name of the association.</p>"""
    priority: NotRequired["aws_sdk_route53resolver.types.priority.Priority"]
    """<p>The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from rule group with the lowest numeric priority setting. </p>"""
    mutation_protection: NotRequired[
        "aws_sdk_route53resolver.types.mutation_protection_status.MutationProtectionStatus"
    ]
    """<p>If enabled, this setting disallows modification or removal of the association, to help prevent against accidentally altering DNS firewall protections. </p>"""
    managed_owner_name: NotRequired[
        "aws_sdk_route53resolver.types.service_principle.ServicePrinciple"
    ]
    """<p>The owner of the association, used only for associations that are not managed by you. If you use Firewall Manager to manage your DNS Firewalls, then this reports Firewall Manager as the managed owner.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_association_status.FirewallRuleGroupAssociationStatus"
    ]
    """<p>The current status of the association.</p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the response, if available.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of running the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    creation_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the association was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "aws_sdk_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the association was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRuleGroupAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "firewall_rule_group_id" in value:
        out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "mutation_protection" in value:
        import aws_sdk_route53resolver.types.mutation_protection_status

        out["MutationProtection"] = (
            aws_sdk_route53resolver.types.mutation_protection_status.serialize_aws_json_1_1(
                value["mutation_protection"]
            )
        )
    if "managed_owner_name" in value:
        out["ManagedOwnerName"] = value["managed_owner_name"]
    if "status" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group_association_status

        out["Status"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRuleGroupAssociation:
    out: FirewallRuleGroupAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "FirewallRuleGroupId" in data:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "MutationProtection" in data:
        import aws_sdk_route53resolver.types.mutation_protection_status

        out["mutation_protection"] = (
            aws_sdk_route53resolver.types.mutation_protection_status.deserialize_aws_json_1_1(
                data["MutationProtection"]
            )
        )
    if "ManagedOwnerName" in data:
        out["managed_owner_name"] = data["ManagedOwnerName"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group_association_status

        out["status"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "ModificationTime" in data:
        out["modification_time"] = data["ModificationTime"]
    return out
