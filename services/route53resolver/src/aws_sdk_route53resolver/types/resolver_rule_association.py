"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resolver_rule_association_status
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.status_message


class ResolverRuleAssociation(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    r"""<p>The ID of the association between a Resolver rule and a VPC. Resolver assigns this value when you submit an <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverRule.html\">AssociateResolverRule</a> request.</p>"""
    resolver_rule_id: NotRequired[
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the Resolver rule that you associated with the VPC that is specified by <code>VPCId</code>.</p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The name of an association between a Resolver rule and a VPC.</p> <p>The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (_), and spaces. The name cannot consist of only numbers.</p>"""
    vpc_id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the VPC that you associated the Resolver rule with.</p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rule_association_status.ResolverRuleAssociationStatus"
    ]
    """<p>A code that specifies the current status of the association between a Resolver rule and a VPC.</p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>A detailed description of the status of the association between a Resolver rule and a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resolver_rule_id" in value:
        out["ResolverRuleId"] = value["resolver_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "vpc_id" in value:
        out["VPCId"] = value["vpc_id"]
    if "status" in value:
        import aws_sdk_route53resolver.types.resolver_rule_association_status

        out["Status"] = (
            aws_sdk_route53resolver.types.resolver_rule_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolverRuleAssociation:
    out: ResolverRuleAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResolverRuleId" in data:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.resolver_rule_association_status

        out["status"] = (
            aws_sdk_route53resolver.types.resolver_rule_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
