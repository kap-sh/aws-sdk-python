"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionOfferingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension_offering_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockExtensionOfferingsResult(TypedDict):
    capacity_block_extension_offerings: NotRequired[
        "aws_sdk_ec2.types.capacity_block_extension_offering_set.CapacityBlockExtensionOfferingSet"
    ]
    """<p>The recommended Capacity Block extension offerings for the dates specified.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockExtensionOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "capacity_block_extension_offerings" in value:
        import aws_sdk_ec2.types.capacity_block_extension_offering_set

        aws_sdk_ec2.types.capacity_block_extension_offering_set.serialize_ec2_query(
            value["capacity_block_extension_offerings"],
            pairs,
            f"{prefix}.CapacityBlockExtensionOfferingSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockExtensionOfferingsResult:
    out: DescribeCapacityBlockExtensionOfferingsResult = {}  # type: ignore[typeddict-item]
    if el.find("CapacityBlockExtensionOfferingSet") is not None:
        import aws_sdk_ec2.types.capacity_block_extension_offering_set

        out["capacity_block_extension_offerings"] = (
            aws_sdk_ec2.types.capacity_block_extension_offering_set.deserialize_ec2_query(
                el, "CapacityBlockExtensionOfferingSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
