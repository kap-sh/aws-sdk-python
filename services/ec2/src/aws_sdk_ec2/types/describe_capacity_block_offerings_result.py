"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_offering_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockOfferingsResult(TypedDict, closed=True):
    capacity_block_offerings: NotRequired[
        "aws_sdk_ec2.types.capacity_block_offering_set.CapacityBlockOfferingSet"
    ]
    """<p>The recommended Capacity Block offering for the dates specified.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_block_offerings" in value:
        import aws_sdk_ec2.types.capacity_block_offering_set

        aws_sdk_ec2.types.capacity_block_offering_set.serialize_ec2_query(
            value["capacity_block_offerings"],
            pairs,
            f"{prefix}.CapacityBlockOfferingSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockOfferingsResult:
    out: DescribeCapacityBlockOfferingsResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityBlockOfferingSet") is not None:
        import aws_sdk_ec2.types.capacity_block_offering_set

        out["capacity_block_offerings"] = (
            aws_sdk_ec2.types.capacity_block_offering_set.deserialize_ec2_query(
                el, "CapacityBlockOfferingSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
