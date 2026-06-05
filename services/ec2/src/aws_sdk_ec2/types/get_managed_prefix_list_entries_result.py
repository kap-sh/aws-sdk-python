"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListEntriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.prefix_list_entry_set


class GetManagedPrefixListEntriesResult(TypedDict):
    entries: NotRequired["aws_sdk_ec2.types.prefix_list_entry_set.PrefixListEntrySet"]
    """<p>Information about the prefix list entries.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetManagedPrefixListEntriesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "entries" in value:
        import aws_sdk_ec2.types.prefix_list_entry_set

        aws_sdk_ec2.types.prefix_list_entry_set.serialize_ec2_query(
            value["entries"], pairs, f"{prefix}.EntrySet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetManagedPrefixListEntriesResult:
    out: GetManagedPrefixListEntriesResult = {}  # type: ignore[typeddict-item]
    if el.find("EntrySet") is not None:
        import aws_sdk_ec2.types.prefix_list_entry_set

        out["entries"] = aws_sdk_ec2.types.prefix_list_entry_set.deserialize_ec2_query(
            el, "EntrySet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
