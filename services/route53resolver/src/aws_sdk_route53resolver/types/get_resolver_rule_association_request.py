"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRuleAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetResolverRuleAssociationRequest(TypedDict, closed=True):
    resolver_rule_association_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule association that you want to get information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRuleAssociationRequest) -> dict:
    out: dict = {}
    out["ResolverRuleAssociationId"] = value["resolver_rule_association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRuleAssociationRequest:
    out: GetResolverRuleAssociationRequest = {}  # type: ignore[typeddict-item]
    if "ResolverRuleAssociationId" in data:
        out["resolver_rule_association_id"] = data["ResolverRuleAssociationId"]
    else:
        raise DeserializationError(
            "GetResolverRuleAssociationRequest.resolver_rule_association_id required"
        )
    return out
