"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesListingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_listing_list


class DescribeReservedInstancesListingsResult(TypedDict, closed=True):
    reserved_instances_listings: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_listing_list.ReservedInstancesListingList"
    ]
    """<p>Information about the Reserved Instance listing.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesListingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_instances_listings" in value:
        import aws_sdk_ec2.types.reserved_instances_listing_list

        aws_sdk_ec2.types.reserved_instances_listing_list.serialize_ec2_query(
            value["reserved_instances_listings"],
            pairs,
            f"{prefix}.ReservedInstancesListingsSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesListingsResult:
    out: DescribeReservedInstancesListingsResult = {}  # type: ignore[typeddict-item]
    if el.find("ReservedInstancesListingsSet") is not None:
        import aws_sdk_ec2.types.reserved_instances_listing_list

        out["reserved_instances_listings"] = (
            aws_sdk_ec2.types.reserved_instances_listing_list.deserialize_ec2_query(
                el, "ReservedInstancesListingsSet"
            )
        )
    return out
