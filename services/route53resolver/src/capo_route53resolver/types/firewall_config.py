"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.account_id
    import capo_route53resolver.types.firewall_fail_open_status
    import capo_route53resolver.types.resource_id


class FirewallConfig(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the firewall configuration.</p>"""
    resource_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the VPC that this firewall configuration applies to.</p>"""
    owner_id: NotRequired["capo_route53resolver.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the owner of the VPC that this firewall configuration applies to.</p>"""
    firewall_fail_open: NotRequired[
        "capo_route53resolver.types.firewall_fail_open_status.FirewallFailOpenStatus"
    ]
    """<p>Determines how DNS Firewall operates during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply. </p> <ul> <li> <p>By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall returns a failure error when it is unable to properly evaluate a query. </p> </li> <li> <p>If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them. </p> </li> </ul> <p>This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallConfig) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "firewall_fail_open" in value:
        import capo_route53resolver.types.firewall_fail_open_status

        out["FirewallFailOpen"] = (
            capo_route53resolver.types.firewall_fail_open_status.serialize_aws_json_1_1(
                value["firewall_fail_open"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallConfig:
    out: FirewallConfig = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "FirewallFailOpen" in data:
        import capo_route53resolver.types.firewall_fail_open_status

        out["firewall_fail_open"] = (
            capo_route53resolver.types.firewall_fail_open_status.deserialize_aws_json_1_1(
                data["FirewallFailOpen"]
            )
        )
    return out
