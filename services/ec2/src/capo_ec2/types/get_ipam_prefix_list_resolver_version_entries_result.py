"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverVersionEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_version_entry_set
    import capo_ec2.types.next_token


class GetIpamPrefixListResolverVersionEntriesResult(TypedDict, closed=True):
    entries: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_version_entry_set.IpamPrefixListResolverVersionEntrySet"
    ]
    """<p>The CIDR entries for the specified resolver version.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverVersionEntriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "entries" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_version_entry_set

        capo_ec2.types.ipam_prefix_list_resolver_version_entry_set.serialize_ec2_query(
            value["entries"], pairs, f"{key_prefix}EntrySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverVersionEntriesResult:
    out: GetIpamPrefixListResolverVersionEntriesResult = {}  # type: ignore[typeddict-item]
    if el.find("entrySet") is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_version_entry_set

        out["entries"] = (
            capo_ec2.types.ipam_prefix_list_resolver_version_entry_set.deserialize_ec2_query(
                el, "entrySet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
