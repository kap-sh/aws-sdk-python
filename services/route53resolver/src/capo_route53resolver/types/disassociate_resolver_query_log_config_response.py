"""Generated from Smithy shape ``com.amazonaws.route53resolver#DisassociateResolverQueryLogConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_query_log_config_association


class DisassociateResolverQueryLogConfigResponse(TypedDict, closed=True):
    resolver_query_log_config_association: NotRequired[
        "capo_route53resolver.types.resolver_query_log_config_association.ResolverQueryLogConfigAssociation"
    ]
    """<p>A complex type that contains settings for the association that you deleted between an Amazon VPC and a query logging configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResolverQueryLogConfigResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config_association" in value:
        import capo_route53resolver.types.resolver_query_log_config_association

        out["ResolverQueryLogConfigAssociation"] = (
            capo_route53resolver.types.resolver_query_log_config_association.serialize_aws_json_1_1(
                value["resolver_query_log_config_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateResolverQueryLogConfigResponse:
    out: DisassociateResolverQueryLogConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfigAssociation" in data:
        import capo_route53resolver.types.resolver_query_log_config_association

        out["resolver_query_log_config_association"] = (
            capo_route53resolver.types.resolver_query_log_config_association.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfigAssociation"]
            )
        )
    return out
