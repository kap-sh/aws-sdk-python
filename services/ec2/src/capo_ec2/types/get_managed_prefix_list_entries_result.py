"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListEntriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.prefix_list_entry_set


class GetManagedPrefixListEntriesResult(TypedDict, closed=True):
    entries: NotRequired["capo_ec2.types.prefix_list_entry_set.PrefixListEntrySet"]
    """<p>Information about the prefix list entries.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetManagedPrefixListEntriesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "entries" in value:
        import capo_ec2.types.prefix_list_entry_set

        capo_ec2.types.prefix_list_entry_set.serialize_ec2_query(
            value["entries"], pairs, f"{key_prefix}EntrySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetManagedPrefixListEntriesResult:
    out: GetManagedPrefixListEntriesResult = {}  # type: ignore[typeddict-item]
    child_entries = el.find("entrySet")
    if child_entries is not None:
        import capo_ec2.types.prefix_list_entry_set

        out["entries"] = capo_ec2.types.prefix_list_entry_set.deserialize_ec2_query(
            child_entries
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
