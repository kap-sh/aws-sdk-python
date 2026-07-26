"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_config


class GetFirewallConfigResponse(TypedDict, closed=True):
    firewall_config: NotRequired[
        "capo_route53resolver.types.firewall_config.FirewallConfig"
    ]
    """<p>Configuration of the firewall behavior provided by DNS Firewall for a single VPC from AmazonVPC. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallConfigResponse) -> dict:
    out: dict = {}
    if "firewall_config" in value:
        import capo_route53resolver.types.firewall_config

        out["FirewallConfig"] = (
            capo_route53resolver.types.firewall_config.serialize_aws_json_1_1(
                value["firewall_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallConfigResponse:
    out: GetFirewallConfigResponse = {}  # type: ignore[typeddict-item]
    if "FirewallConfig" in data:
        import capo_route53resolver.types.firewall_config

        out["firewall_config"] = (
            capo_route53resolver.types.firewall_config.deserialize_aws_json_1_1(
                data["FirewallConfig"]
            )
        )
    return out
