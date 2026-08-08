"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionHistoryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_extension_set
    import capo_ec2.types.string


class DescribeCapacityBlockExtensionHistoryResult(TypedDict, closed=True):
    capacity_block_extensions: NotRequired[
        "capo_ec2.types.capacity_block_extension_set.CapacityBlockExtensionSet"
    ]
    """<p>Describes one or more of your Capacity Block extensions. The results describe only the Capacity Block extensions in the Amazon Web Services Region that you're currently using.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockExtensionHistoryResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_block_extensions" in value:
        import capo_ec2.types.capacity_block_extension_set

        capo_ec2.types.capacity_block_extension_set.serialize_ec2_query(
            value["capacity_block_extensions"],
            pairs,
            f"{key_prefix}CapacityBlockExtensionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockExtensionHistoryResult:
    out: DescribeCapacityBlockExtensionHistoryResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityBlockExtensionSet") is not None:
        import capo_ec2.types.capacity_block_extension_set

        out["capacity_block_extensions"] = (
            capo_ec2.types.capacity_block_extension_set.deserialize_ec2_query(
                el, "capacityBlockExtensionSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
