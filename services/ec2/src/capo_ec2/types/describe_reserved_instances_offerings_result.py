"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_offering_list
    import capo_ec2.types.string


class DescribeReservedInstancesOfferingsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    reserved_instances_offerings: NotRequired[
        "capo_ec2.types.reserved_instances_offering_list.ReservedInstancesOfferingList"
    ]
    """<p>A list of Reserved Instances offerings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesOfferingsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "reserved_instances_offerings" in value:
        import capo_ec2.types.reserved_instances_offering_list

        capo_ec2.types.reserved_instances_offering_list.serialize_ec2_query(
            value["reserved_instances_offerings"],
            pairs,
            f"{key_prefix}ReservedInstancesOfferingsSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesOfferingsResult:
    out: DescribeReservedInstancesOfferingsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_reserved_instances_offerings = el.find("reservedInstancesOfferingsSet")
    if child_reserved_instances_offerings is not None:
        import capo_ec2.types.reserved_instances_offering_list

        out["reserved_instances_offerings"] = (
            capo_ec2.types.reserved_instances_offering_list.deserialize_ec2_query(
                child_reserved_instances_offerings
            )
        )
    return out
