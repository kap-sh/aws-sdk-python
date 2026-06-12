"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResolverQueryLogConfigAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association

ResolverQueryLogConfigAssociationList: TypeAlias = list[
    "aws_sdk_route53resolver.types.resolver_query_log_config_association.ResolverQueryLogConfigAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolverQueryLogConfigAssociationList) -> list:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53resolver.types.resolver_query_log_config_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolverQueryLogConfigAssociationList:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association

    out: ResolverQueryLogConfigAssociationList = []
    for item in data:
        out.append(
            aws_sdk_route53resolver.types.resolver_query_log_config_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
