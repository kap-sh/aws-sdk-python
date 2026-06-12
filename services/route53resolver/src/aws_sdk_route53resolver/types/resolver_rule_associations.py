"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverRuleAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_rule_association

ResolverRuleAssociations: TypeAlias = list[
    "aws_sdk_route53resolver.types.resolver_rule_association.ResolverRuleAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverRuleAssociations) -> list:
    import aws_sdk_route53resolver.types.resolver_rule_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.resolver_rule_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverRuleAssociations:
    import aws_sdk_route53resolver.types.resolver_rule_association

    out: ResolverRuleAssociations = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.resolver_rule_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
