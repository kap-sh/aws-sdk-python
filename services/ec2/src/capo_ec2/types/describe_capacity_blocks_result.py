"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlocksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_set
    import capo_ec2.types.string


class DescribeCapacityBlocksResult(TypedDict, closed=True):
    capacity_blocks: NotRequired["capo_ec2.types.capacity_block_set.CapacityBlockSet"]
    """<p>The Capacity Blocks.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlocksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_blocks" in value:
        import capo_ec2.types.capacity_block_set

        capo_ec2.types.capacity_block_set.serialize_ec2_query(
            value["capacity_blocks"], pairs, f"{key_prefix}CapacityBlockSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlocksResult:
    out: DescribeCapacityBlocksResult = {}  # type: ignore[typeddict-item]
    child_capacity_blocks = el.find("capacityBlockSet")
    if child_capacity_blocks is not None:
        import capo_ec2.types.capacity_block_set

        out["capacity_blocks"] = (
            capo_ec2.types.capacity_block_set.deserialize_ec2_query(
                child_capacity_blocks
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
