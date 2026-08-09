"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeManagedPrefixListsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.managed_prefix_list_set
    import capo_ec2.types.next_token


class DescribeManagedPrefixListsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    prefix_lists: NotRequired[
        "capo_ec2.types.managed_prefix_list_set.ManagedPrefixListSet"
    ]
    """<p>Information about the prefix lists.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeManagedPrefixListsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "prefix_lists" in value:
        import capo_ec2.types.managed_prefix_list_set

        capo_ec2.types.managed_prefix_list_set.serialize_ec2_query(
            value["prefix_lists"], pairs, f"{key_prefix}PrefixListSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeManagedPrefixListsResult:
    out: DescribeManagedPrefixListsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_prefix_lists = el.find("prefixListSet")
    if child_prefix_lists is not None:
        import capo_ec2.types.managed_prefix_list_set

        out["prefix_lists"] = (
            capo_ec2.types.managed_prefix_list_set.deserialize_ec2_query(
                child_prefix_lists
            )
        )
    return out
