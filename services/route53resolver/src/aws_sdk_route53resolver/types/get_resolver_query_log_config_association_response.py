"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_query_log_config_association


class GetResolverQueryLogConfigAssociationResponse(TypedDict, closed=True):
    resolver_query_log_config_association: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_association.ResolverQueryLogConfigAssociation"
    ]
    """<p>Information about the Resolver query logging configuration association that you specified in a <code>GetQueryLogConfigAssociation</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigAssociationResponse) -> dict:
    out: dict = {}
    if "resolver_query_log_config_association" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association

        out["ResolverQueryLogConfigAssociation"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association.serialize_aws_json_1_1(
                value["resolver_query_log_config_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetResolverQueryLogConfigAssociationResponse:
    out: GetResolverQueryLogConfigAssociationResponse = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfigAssociation" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_association

        out["resolver_query_log_config_association"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_association.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfigAssociation"]
            )
        )
    return out
