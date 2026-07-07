"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.firewall
    import aws_sdk_network_firewall.types.firewall_status


class DeleteFirewallResponse(TypedDict, closed=True):
    firewall: NotRequired["aws_sdk_network_firewall.types.firewall.Firewall"]
    firewall_status: NotRequired[
        "aws_sdk_network_firewall.types.firewall_status.FirewallStatus"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallResponse) -> dict:
    out: dict = {}
    if "firewall" in value:
        import aws_sdk_network_firewall.types.firewall

        out["Firewall"] = (
            aws_sdk_network_firewall.types.firewall.serialize_aws_json_1_0(
                value["firewall"]
            )
        )
    if "firewall_status" in value:
        import aws_sdk_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            aws_sdk_network_firewall.types.firewall_status.serialize_aws_json_1_0(
                value["firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallResponse:
    out: DeleteFirewallResponse = {}  # type: ignore[typeddict-item]
    if "Firewall" in data:
        import aws_sdk_network_firewall.types.firewall

        out["firewall"] = (
            aws_sdk_network_firewall.types.firewall.deserialize_aws_json_1_0(
                data["Firewall"]
            )
        )
    if "FirewallStatus" in data:
        import aws_sdk_network_firewall.types.firewall_status

        out["firewall_status"] = (
            aws_sdk_network_firewall.types.firewall_status.deserialize_aws_json_1_0(
                data["FirewallStatus"]
            )
        )
    return out
