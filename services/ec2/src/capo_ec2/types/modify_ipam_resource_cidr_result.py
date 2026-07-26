"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_cidr


class ModifyIpamResourceCidrResult(TypedDict, closed=True):
    ipam_resource_cidr: NotRequired[
        "capo_ec2.types.ipam_resource_cidr.IpamResourceCidr"
    ]
    """<p>The CIDR of the resource.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamResourceCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_resource_cidr" in value:
        import capo_ec2.types.ipam_resource_cidr

        capo_ec2.types.ipam_resource_cidr.serialize_ec2_query(
            value["ipam_resource_cidr"], pairs, f"{prefix}.IpamResourceCidr"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamResourceCidrResult:
    out: ModifyIpamResourceCidrResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_cidr = el.find("IpamResourceCidr")
    if child_ipam_resource_cidr is not None:
        import capo_ec2.types.ipam_resource_cidr

        out["ipam_resource_cidr"] = (
            capo_ec2.types.ipam_resource_cidr.deserialize_ec2_query(
                child_ipam_resource_cidr
            )
        )
    return out
