"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationBillingRequestsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_billing_request_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationBillingRequestsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_billing_requests: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_billing_request_set.CapacityReservationBillingRequestSet"
    ]
    """<p>Information about the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationBillingRequestsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "capacity_reservation_billing_requests" in value:
        import aws_sdk_ec2.types.capacity_reservation_billing_request_set

        aws_sdk_ec2.types.capacity_reservation_billing_request_set.serialize_ec2_query(
            value["capacity_reservation_billing_requests"],
            pairs,
            f"{prefix}.CapacityReservationBillingRequestSet",
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityReservationBillingRequestsResult:
    out: DescribeCapacityReservationBillingRequestsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("CapacityReservationBillingRequestSet") is not None:
        import aws_sdk_ec2.types.capacity_reservation_billing_request_set

        out["capacity_reservation_billing_requests"] = (
            aws_sdk_ec2.types.capacity_reservation_billing_request_set.deserialize_ec2_query(
                el, "CapacityReservationBillingRequestSet"
            )
        )
    return out
