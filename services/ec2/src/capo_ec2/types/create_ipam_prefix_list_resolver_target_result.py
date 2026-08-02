"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverTargetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_target


class CreateIpamPrefixListResolverTargetResult(TypedDict, closed=True):
    ipam_prefix_list_resolver_target: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_target.IpamPrefixListResolverTarget"
    ]
    """<p>Information about the IPAM prefix list resolver target that was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamPrefixListResolverTargetResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_prefix_list_resolver_target" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_target

        capo_ec2.types.ipam_prefix_list_resolver_target.serialize_ec2_query(
            value["ipam_prefix_list_resolver_target"],
            pairs,
            f"{key_prefix}IpamPrefixListResolverTarget",
        )


def deserialize_ec2_query(el: Element) -> CreateIpamPrefixListResolverTargetResult:
    out: CreateIpamPrefixListResolverTargetResult = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver_target = el.find("IpamPrefixListResolverTarget")
    if child_ipam_prefix_list_resolver_target is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_target

        out["ipam_prefix_list_resolver_target"] = (
            capo_ec2.types.ipam_prefix_list_resolver_target.deserialize_ec2_query(
                child_ipam_prefix_list_resolver_target
            )
        )
    return out
