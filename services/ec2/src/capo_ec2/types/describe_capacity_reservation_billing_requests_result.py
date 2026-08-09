"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationBillingRequestsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_billing_request_set
    import capo_ec2.types.string


class DescribeCapacityReservationBillingRequestsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_billing_requests: NotRequired[
        "capo_ec2.types.capacity_reservation_billing_request_set.CapacityReservationBillingRequestSet"
    ]
    """<p>Information about the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityReservationBillingRequestsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "capacity_reservation_billing_requests" in value:
        import capo_ec2.types.capacity_reservation_billing_request_set

        capo_ec2.types.capacity_reservation_billing_request_set.serialize_ec2_query(
            value["capacity_reservation_billing_requests"],
            pairs,
            f"{key_prefix}CapacityReservationBillingRequestSet",
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeCapacityReservationBillingRequestsResult:
    out: DescribeCapacityReservationBillingRequestsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_capacity_reservation_billing_requests = el.find(
        "capacityReservationBillingRequestSet"
    )
    if child_capacity_reservation_billing_requests is not None:
        import capo_ec2.types.capacity_reservation_billing_request_set

        out["capacity_reservation_billing_requests"] = (
            capo_ec2.types.capacity_reservation_billing_request_set.deserialize_ec2_query(
                child_capacity_reservation_billing_requests
            )
        )
    return out
