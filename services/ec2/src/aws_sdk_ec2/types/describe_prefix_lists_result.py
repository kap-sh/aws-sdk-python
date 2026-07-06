"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePrefixListsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_set
    import aws_sdk_ec2.types.string


class DescribePrefixListsResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    prefix_lists: NotRequired["aws_sdk_ec2.types.prefix_list_set.PrefixListSet"]
    """<p>All available prefix lists.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePrefixListsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "prefix_lists" in value:
        import aws_sdk_ec2.types.prefix_list_set

        aws_sdk_ec2.types.prefix_list_set.serialize_ec2_query(
            value["prefix_lists"], pairs, f"{prefix}.PrefixListSet"
        )


def deserialize_ec2_query(el: Element) -> DescribePrefixListsResult:
    out: DescribePrefixListsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("PrefixListSet") is not None:
        import aws_sdk_ec2.types.prefix_list_set

        out["prefix_lists"] = aws_sdk_ec2.types.prefix_list_set.deserialize_ec2_query(
            el, "PrefixListSet"
        )
    return out
