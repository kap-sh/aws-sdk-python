"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeCapacityReservationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.decrease_requests_remaining
    import capo_elastic_load_balancing_v2.types.last_modified_time
    import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity
    import capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states


class DescribeCapacityReservationOutput(TypedDict, closed=True):
    last_modified_time: NotRequired[
        "capo_elastic_load_balancing_v2.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last time the capacity reservation was modified.</p>"""
    decrease_requests_remaining: NotRequired[
        "capo_elastic_load_balancing_v2.types.decrease_requests_remaining.DecreaseRequestsRemaining"
    ]
    """<p>The amount of daily capacity decreases remaining.</p>"""
    minimum_load_balancer_capacity: NotRequired[
        "capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.MinimumLoadBalancerCapacity"
    ]
    """<p>The requested minimum capacity reservation for the load balancer</p>"""
    capacity_reservation_state: NotRequired[
        "capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states.ZonalCapacityReservationStates"
    ]
    """<p>The state of the capacity reservation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCapacityReservationOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "last_modified_time" in value:
        import capo_elastic_load_balancing_v2.types.last_modified_time

        capo_elastic_load_balancing_v2.types.last_modified_time.serialize_query(
            value["last_modified_time"], pairs, f"{prefix}.LastModifiedTime"
        )
    if "decrease_requests_remaining" in value:
        pairs.append(
            (
                f"{prefix}.DecreaseRequestsRemaining",
                str(value["decrease_requests_remaining"]),
            )
        )
    if "minimum_load_balancer_capacity" in value:
        import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity

        capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.serialize_query(
            value["minimum_load_balancer_capacity"],
            pairs,
            f"{prefix}.MinimumLoadBalancerCapacity",
        )
    if "capacity_reservation_state" in value:
        import capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states

        capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states.serialize_query(
            value["capacity_reservation_state"],
            pairs,
            f"{prefix}.CapacityReservationState",
        )


def deserialize_query(el: Element) -> DescribeCapacityReservationOutput:
    out: DescribeCapacityReservationOutput = {}  # type: ignore[typeddict-item]
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_elastic_load_balancing_v2.types.last_modified_time

        out["last_modified_time"] = (
            capo_elastic_load_balancing_v2.types.last_modified_time.deserialize_query(
                child_last_modified_time
            )
        )
    child_decrease_requests_remaining = el.find("DecreaseRequestsRemaining")
    if child_decrease_requests_remaining is not None:
        out["decrease_requests_remaining"] = int(
            child_decrease_requests_remaining.text or ""
        )
    child_minimum_load_balancer_capacity = el.find("MinimumLoadBalancerCapacity")
    if child_minimum_load_balancer_capacity is not None:
        import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity

        out["minimum_load_balancer_capacity"] = (
            capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.deserialize_query(
                child_minimum_load_balancer_capacity
            )
        )
    child_capacity_reservation_state = el.find("CapacityReservationState")
    if child_capacity_reservation_state is not None:
        import capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states

        out["capacity_reservation_state"] = (
            capo_elastic_load_balancing_v2.types.zonal_capacity_reservation_states.deserialize_query(
                child_capacity_reservation_state
            )
        )
    return out
