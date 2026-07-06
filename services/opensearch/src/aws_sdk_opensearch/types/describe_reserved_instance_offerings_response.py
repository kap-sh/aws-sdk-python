"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeReservedInstanceOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.next_token
    import aws_sdk_opensearch.types.reserved_instance_offering_list


class DescribeReservedInstanceOfferingsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""
    reserved_instance_offerings: NotRequired[
        "aws_sdk_opensearch.types.reserved_instance_offering_list.ReservedInstanceOfferingList"
    ]
    """<p>List of Reserved Instance offerings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservedInstanceOfferingsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "reserved_instance_offerings" in value:
        import aws_sdk_opensearch.types.reserved_instance_offering_list

        out["ReservedInstanceOfferings"] = (
            aws_sdk_opensearch.types.reserved_instance_offering_list.serialize_json(
                value["reserved_instance_offerings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeReservedInstanceOfferingsResponse:
    out: DescribeReservedInstanceOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ReservedInstanceOfferings" in data:
        import aws_sdk_opensearch.types.reserved_instance_offering_list

        out["reserved_instance_offerings"] = (
            aws_sdk_opensearch.types.reserved_instance_offering_list.deserialize_json(
                data["ReservedInstanceOfferings"]
            )
        )
    return out
