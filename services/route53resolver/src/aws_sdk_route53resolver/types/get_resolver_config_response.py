"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_config


class GetResolverConfigResponse(TypedDict, closed=True):
    resolver_config: NotRequired[
        "aws_sdk_route53resolver.types.resolver_config.ResolverConfig"
    ]
    """<p>Information about the behavior configuration of Route 53 Resolver behavior for the VPC you specified in the <code>GetResolverConfig</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverConfigResponse) -> dict:
    out: dict = {}
    if "resolver_config" in value:
        import aws_sdk_route53resolver.types.resolver_config

        out["ResolverConfig"] = (
            aws_sdk_route53resolver.types.resolver_config.serialize_aws_json_1_1(
                value["resolver_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverConfigResponse:
    out: GetResolverConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverConfig" in data:
        import aws_sdk_route53resolver.types.resolver_config

        out["resolver_config"] = (
            aws_sdk_route53resolver.types.resolver_config.deserialize_aws_json_1_1(
                data["ResolverConfig"]
            )
        )
    return out
