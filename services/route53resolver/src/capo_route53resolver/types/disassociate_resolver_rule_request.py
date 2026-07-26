"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.resource_id


class DisassociateResolverRuleRequest(TypedDict, closed=True):
    vpc_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the VPC that you want to disassociate the Resolver rule from.</p>"""
    resolver_rule_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to disassociate from the specified VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResolverRuleRequest) -> dict:
    out: dict = {}
    out["VPCId"] = value["vpc_id"]
    out["ResolverRuleId"] = value["resolver_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateResolverRuleRequest:
    out: DisassociateResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if "VPCId" in data:
        out["vpc_id"] = data["VPCId"]
    else:
        raise DeserializationError("DisassociateResolverRuleRequest.vpc_id required")
    if "ResolverRuleId" in data:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        raise DeserializationError(
            "DisassociateResolverRuleRequest.resolver_rule_id required"
        )
    return out
