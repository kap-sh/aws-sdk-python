"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverDnssecConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.resolver_dnssec_config


class GetResolverDnssecConfigResponse(TypedDict, closed=True):
    resolver_dnssec_config: NotRequired[
        "capo_route53resolver.types.resolver_dnssec_config.ResolverDnssecConfig"
    ]
    """<p>The information about a configuration for DNSSEC validation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverDnssecConfigResponse) -> dict:
    out: dict = {}
    if "resolver_dnssec_config" in value:
        import capo_route53resolver.types.resolver_dnssec_config

        out["ResolverDNSSECConfig"] = (
            capo_route53resolver.types.resolver_dnssec_config.serialize_aws_json_1_1(
                value["resolver_dnssec_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverDnssecConfigResponse:
    out: GetResolverDnssecConfigResponse = {}  # type: ignore[typeddict-item]
    if "ResolverDNSSECConfig" in data:
        import capo_route53resolver.types.resolver_dnssec_config

        out["resolver_dnssec_config"] = (
            capo_route53resolver.types.resolver_dnssec_config.deserialize_aws_json_1_1(
                data["ResolverDNSSECConfig"]
            )
        )
    return out
