"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlocksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlocksResult(TypedDict):
    capacity_blocks: NotRequired[
        "aws_sdk_ec2.types.capacity_block_set.CapacityBlockSet"
    ]
    """<p>The Capacity Blocks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlocksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_blocks" in value:
        import aws_sdk_ec2.types.capacity_block_set

        aws_sdk_ec2.types.capacity_block_set.serialize_ec2_query(
            value["capacity_blocks"], pairs, f"{prefix}.CapacityBlockSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlocksResult:
    out: DescribeCapacityBlocksResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityBlockSet") is not None:
        import aws_sdk_ec2.types.capacity_block_set

        out["capacity_blocks"] = (
            aws_sdk_ec2.types.capacity_block_set.deserialize_ec2_query(
                el, "CapacityBlockSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
