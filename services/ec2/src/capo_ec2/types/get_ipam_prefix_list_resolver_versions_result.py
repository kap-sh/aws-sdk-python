"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverVersionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_version_set
    import capo_ec2.types.next_token


class GetIpamPrefixListResolverVersionsResult(TypedDict, closed=True):
    ipam_prefix_list_resolver_versions: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_version_set.IpamPrefixListResolverVersionSet"
    ]
    """<p>Information about the IPAM prefix list resolver versions.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverVersionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_prefix_list_resolver_versions" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_version_set

        capo_ec2.types.ipam_prefix_list_resolver_version_set.serialize_ec2_query(
            value["ipam_prefix_list_resolver_versions"],
            pairs,
            f"{key_prefix}IpamPrefixListResolverVersionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverVersionsResult:
    out: GetIpamPrefixListResolverVersionsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamPrefixListResolverVersionSet") is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_version_set

        out["ipam_prefix_list_resolver_versions"] = (
            capo_ec2.types.ipam_prefix_list_resolver_version_set.deserialize_ec2_query(
                el, "IpamPrefixListResolverVersionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
