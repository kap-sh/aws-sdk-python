"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateResolverQueryLogConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association


class AssociateResolverQueryLogConfigResponse(TypedDict, closed=True):
    resolver_query_log_config_association: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_association.ResolverQueryLogConfigAssociation"
    ]
    """<p>A complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResolverQueryLogConfigResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config_association" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association

        out["ResolverQueryLogConfigAssociation"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association.serialize_aws_json_1_1(
                value["resolver_query_log_config_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResolverQueryLogConfigResponse:
    out: AssociateResolverQueryLogConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfigAssociation" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association

        out["resolver_query_log_config_association"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfigAssociation"]
            )
        )
    return out
