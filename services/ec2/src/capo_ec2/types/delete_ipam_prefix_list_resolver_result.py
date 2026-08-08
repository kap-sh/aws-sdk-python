"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver


class DeleteIpamPrefixListResolverResult(TypedDict, closed=True):
    ipam_prefix_list_resolver: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver.IpamPrefixListResolver"
    ]
    """<p>Information about the IPAM prefix list resolver that was deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPrefixListResolverResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_prefix_list_resolver" in value:
        import capo_ec2.types.ipam_prefix_list_resolver

        capo_ec2.types.ipam_prefix_list_resolver.serialize_ec2_query(
            value["ipam_prefix_list_resolver"],
            pairs,
            f"{key_prefix}IpamPrefixListResolver",
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPrefixListResolverResult:
    out: DeleteIpamPrefixListResolverResult = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver = el.find("ipamPrefixListResolver")
    if child_ipam_prefix_list_resolver is not None:
        import capo_ec2.types.ipam_prefix_list_resolver

        out["ipam_prefix_list_resolver"] = (
            capo_ec2.types.ipam_prefix_list_resolver.deserialize_ec2_query(
                child_ipam_prefix_list_resolver
            )
        )
    return out
