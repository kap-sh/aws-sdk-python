"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resolver_config


class UpdateResolverConfigResponse(TypedDict):
    resolver_config: NotRequired[
        "aws_sdk_route53resolver.types.resolver_config.ResolverConfig"
    ]
    """<p>An array that contains settings for the specified Resolver configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverConfigResponse) -> dict:
    out: dict = {}
    if "resolver_config" in value:
        import aws_sdk_route53resolver.types.resolver_config

        out["ResolverConfig"] = (
            aws_sdk_route53resolver.types.resolver_config.serialize_aws_json_1_1(
                value["resolver_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverConfigResponse:
    out: UpdateResolverConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverConfig" in data:
        import aws_sdk_route53resolver.types.resolver_config

        out["resolver_config"] = (
            aws_sdk_route53resolver.types.resolver_config.deserialize_aws_json_1_1(
                data["ResolverConfig"]
            )
        )
    return out
