"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_rule


class UpdateResolverRuleResponse(TypedDict, closed=True):
    resolver_rule: NotRequired["capo_route53resolver.types.resolver_rule.ResolverRule"]
    """<p>The response to an <code>UpdateResolverRule</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverRuleResponse) -> dict:
    out: dict = {}
    if "resolver_rule" in value:
        import capo_route53resolver.types.resolver_rule

        out["ResolverRule"] = (
            capo_route53resolver.types.resolver_rule.serialize_aws_json_1_1(
                value["resolver_rule"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverRuleResponse:
    out: UpdateResolverRuleResponse = {}  # type: ignore[typeddict-item]
    if "ResolverRule" in data:
        import capo_route53resolver.types.resolver_rule

        out["resolver_rule"] = (
            capo_route53resolver.types.resolver_rule.deserialize_aws_json_1_1(
                data["ResolverRule"]
            )
        )
    return out
