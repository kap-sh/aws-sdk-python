"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_config


class UpdateFirewallConfigResponse(TypedDict, closed=True):
    firewall_config: NotRequired[
        "aws_sdk_route53resolver.types.firewall_config.FirewallConfig"
    ]
    """<p>Configuration of the firewall behavior provided by DNS Firewall for a single VPC. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallConfigResponse) -> dict:
    out: dict = {}
    if "firewall_config" in value:
        import aws_sdk_route53resolver.types.firewall_config

        out["FirewallConfig"] = (
            aws_sdk_route53resolver.types.firewall_config.serialize_aws_json_1_1(
                value["firewall_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFirewallConfigResponse:
    out: UpdateFirewallConfigResponse = {}  # type: ignore[typeddict-item]
    if "FirewallConfig" in data:
        import aws_sdk_route53resolver.types.firewall_config

        out["firewall_config"] = (
            aws_sdk_route53resolver.types.firewall_config.deserialize_aws_json_1_1(
                data["FirewallConfig"]
            )
        )
    return out
