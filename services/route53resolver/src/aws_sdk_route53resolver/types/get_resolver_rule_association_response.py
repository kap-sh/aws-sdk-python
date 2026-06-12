"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRuleAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_rule_association


class GetResolverRuleAssociationResponse(TypedDict):
    resolver_rule_association: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rule_association.ResolverRuleAssociation"
    ]
    """<p>Information about the Resolver rule association that you specified in a <code>GetResolverRuleAssociation</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRuleAssociationResponse) -> dict:
    out: dict = {}
    if "resolver_rule_association" in value:
        import aws_sdk_route53resolver.types.resolver_rule_association

        out["ResolverRuleAssociation"] = (
            aws_sdk_route53resolver.types.resolver_rule_association.serialize_aws_json_1_1(
                value["resolver_rule_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRuleAssociationResponse:
    out: GetResolverRuleAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ResolverRuleAssociation" in data:
        import aws_sdk_route53resolver.types.resolver_rule_association

        out["resolver_rule_association"] = (
            aws_sdk_route53resolver.types.resolver_rule_association.deserialize_aws_json_1_1(
                data["ResolverRuleAssociation"]
            )
        )
    return out
