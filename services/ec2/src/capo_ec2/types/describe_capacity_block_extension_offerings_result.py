"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_block_extension_offering_set
    import capo_ec2.types.string


class DescribeCapacityBlockExtensionOfferingsResult(TypedDict, closed=True):
    capacity_block_extension_offerings: NotRequired[
        "capo_ec2.types.capacity_block_extension_offering_set.CapacityBlockExtensionOfferingSet"
    ]
    """<p>The recommended Capacity Block extension offerings for the dates specified.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockExtensionOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_block_extension_offerings" in value:
        import capo_ec2.types.capacity_block_extension_offering_set

        capo_ec2.types.capacity_block_extension_offering_set.serialize_ec2_query(
            value["capacity_block_extension_offerings"],
            pairs,
            f"{key_prefix}CapacityBlockExtensionOfferingSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockExtensionOfferingsResult:
    out: DescribeCapacityBlockExtensionOfferingsResult = {}  # type: ignore[typeddict-item]
    if el.find("capacityBlockExtensionOfferingSet") is not None:
        import capo_ec2.types.capacity_block_extension_offering_set

        out["capacity_block_extension_offerings"] = (
            capo_ec2.types.capacity_block_extension_offering_set.deserialize_ec2_query(
                el, "capacityBlockExtensionOfferingSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
