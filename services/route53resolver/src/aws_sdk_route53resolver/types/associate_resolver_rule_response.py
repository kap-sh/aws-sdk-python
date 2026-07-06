"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateResolverRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_rule_association


class AssociateResolverRuleResponse(TypedDict, closed=True):
    resolver_rule_association: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rule_association.ResolverRuleAssociation"
    ]
    """<p>Information about the <code>AssociateResolverRule</code> request, including the status of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResolverRuleResponse) -> dict:
    out: dict = {}
    if "resolver_rule_association" in value:
        import aws_sdk_route53resolver.types.resolver_rule_association

        out["ResolverRuleAssociation"] = (
            aws_sdk_route53resolver.types.resolver_rule_association.serialize_aws_json_1_1(
                value["resolver_rule_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResolverRuleResponse:
    out: AssociateResolverRuleResponse = {}  # type: ignore[typeddict-item]
    if "ResolverRuleAssociation" in data:
        import aws_sdk_route53resolver.types.resolver_rule_association

        out["resolver_rule_association"] = (
            aws_sdk_route53resolver.types.resolver_rule_association.deserialize_aws_json_1_1(
                data["ResolverRuleAssociation"]
            )
        )
    return out
