"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery


class DeleteIpamResourceDiscoveryResult(TypedDict, closed=True):
    ipam_resource_discovery: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery.IpamResourceDiscovery"
    ]
    """<p>The IPAM resource discovery.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamResourceDiscoveryResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_resource_discovery" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery

        aws_sdk_ec2.types.ipam_resource_discovery.serialize_ec2_query(
            value["ipam_resource_discovery"], pairs, f"{prefix}.IpamResourceDiscovery"
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamResourceDiscoveryResult:
    out: DeleteIpamResourceDiscoveryResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discovery = el.find("IpamResourceDiscovery")
    if child_ipam_resource_discovery is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery

        out["ipam_resource_discovery"] = (
            aws_sdk_ec2.types.ipam_resource_discovery.deserialize_ec2_query(
                child_ipam_resource_discovery
            )
        )
    return out
