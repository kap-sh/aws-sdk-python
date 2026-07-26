"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_rule

ResolverRules: TypeAlias = list["capo_route53resolver.types.resolver_rule.ResolverRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRules) -> list:
    import capo_route53resolver.types.resolver_rule

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.resolver_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverRules:
    import capo_route53resolver.types.resolver_rule

    out: ResolverRules = []
    for item in data:
        out.append(
            capo_route53resolver.types.resolver_rule.deserialize_aws_json_1_1(item)
        )
    return out
