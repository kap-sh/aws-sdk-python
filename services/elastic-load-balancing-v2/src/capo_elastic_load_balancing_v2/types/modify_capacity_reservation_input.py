"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity
    import capo_elastic_load_balancing_v2.types.reset_capacity_reservation


class ModifyCapacityReservationInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    minimum_load_balancer_capacity: NotRequired[
        "capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.MinimumLoadBalancerCapacity"
    ]
    """<p>The minimum load balancer capacity reserved.</p>"""
    reset_capacity_reservation: NotRequired[
        "capo_elastic_load_balancing_v2.types.reset_capacity_reservation.ResetCapacityReservation"
    ]
    """<p>Resets the capacity reservation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCapacityReservationInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "minimum_load_balancer_capacity" in value:
        import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity

        capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.serialize_query(
            value["minimum_load_balancer_capacity"],
            pairs,
            f"{key_prefix}MinimumLoadBalancerCapacity",
        )
    if "reset_capacity_reservation" in value:
        pairs.append(
            (
                f"{key_prefix}ResetCapacityReservation",
                "true" if value["reset_capacity_reservation"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyCapacityReservationInput:
    out: ModifyCapacityReservationInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_minimum_load_balancer_capacity = el.find("MinimumLoadBalancerCapacity")
    if child_minimum_load_balancer_capacity is not None:
        import capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity

        out["minimum_load_balancer_capacity"] = (
            capo_elastic_load_balancing_v2.types.minimum_load_balancer_capacity.deserialize_query(
                child_minimum_load_balancer_capacity
            )
        )
    child_reset_capacity_reservation = el.find("ResetCapacityReservation")
    if child_reset_capacity_reservation is not None:
        out["reset_capacity_reservation"] = (
            child_reset_capacity_reservation.text or ""
        ).lower() == "true"
    return out
