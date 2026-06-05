"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_offering_list
    import aws_sdk_ec2.types.string


class DescribeReservedInstancesOfferingsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    reserved_instances_offerings: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_list.ReservedInstancesOfferingList"
    ]
    """<p>A list of Reserved Instances offerings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "reserved_instances_offerings" in value:
        import aws_sdk_ec2.types.reserved_instances_offering_list

        aws_sdk_ec2.types.reserved_instances_offering_list.serialize_ec2_query(
            value["reserved_instances_offerings"],
            pairs,
            f"{prefix}.ReservedInstancesOfferingsSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesOfferingsResult:
    out: DescribeReservedInstancesOfferingsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ReservedInstancesOfferingsSet") is not None:
        import aws_sdk_ec2.types.reserved_instances_offering_list

        out["reserved_instances_offerings"] = (
            aws_sdk_ec2.types.reserved_instances_offering_list.deserialize_ec2_query(
                el, "ReservedInstancesOfferingsSet"
            )
        )
    return out
