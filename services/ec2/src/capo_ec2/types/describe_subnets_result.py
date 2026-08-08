"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSubnetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.subnet_list


class DescribeSubnetsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    subnets: NotRequired["capo_ec2.types.subnet_list.SubnetList"]
    """<p>Information about the subnets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSubnetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "subnets" in value:
        import capo_ec2.types.subnet_list

        capo_ec2.types.subnet_list.serialize_ec2_query(
            value["subnets"], pairs, f"{key_prefix}SubnetSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeSubnetsResult:
    out: DescribeSubnetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("subnetSet") is not None:
        import capo_ec2.types.subnet_list

        out["subnets"] = capo_ec2.types.subnet_list.deserialize_ec2_query(
            el, "subnetSet"
        )
    return out
