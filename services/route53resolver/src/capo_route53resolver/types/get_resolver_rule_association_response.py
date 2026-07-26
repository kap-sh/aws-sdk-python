"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRuleAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_rule_association


class GetResolverRuleAssociationResponse(TypedDict, closed=True):
    resolver_rule_association: NotRequired[
        "capo_route53resolver.types.resolver_rule_association.ResolverRuleAssociation"
    ]
    """<p>Information about the Resolver rule association that you specified in a <code>GetResolverRuleAssociation</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRuleAssociationResponse) -> dict:
    out: dict = {}
    if "resolver_rule_association" in value:
        import capo_route53resolver.types.resolver_rule_association

        out["ResolverRuleAssociation"] = (
            capo_route53resolver.types.resolver_rule_association.serialize_aws_json_1_1(
                value["resolver_rule_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRuleAssociationResponse:
    out: GetResolverRuleAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ResolverRuleAssociation" in data:
        import capo_route53resolver.types.resolver_rule_association

        out["resolver_rule_association"] = (
            capo_route53resolver.types.resolver_rule_association.deserialize_aws_json_1_1(
                data["ResolverRuleAssociation"]
            )
        )
    return out
