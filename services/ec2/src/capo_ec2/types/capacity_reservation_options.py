"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_capacity_reservation_usage_strategy


class CapacityReservationOptions(TypedDict, closed=True):
    usage_strategy: NotRequired[
        "capo_ec2.types.fleet_capacity_reservation_usage_strategy.FleetCapacityReservationUsageStrategy"
    ]
    """<p>Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.</p> <p>If you specify <code>use-capacity-reservations-first</code>, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (<code>lowest-price</code> or <code>prioritized</code>) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (<code>lowest-price</code> or <code>prioritized</code>).</p> <p>If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "usage_strategy" in value:
        import capo_ec2.types.fleet_capacity_reservation_usage_strategy

        capo_ec2.types.fleet_capacity_reservation_usage_strategy.serialize_ec2_query(
            value["usage_strategy"], pairs, f"{key_prefix}UsageStrategy"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationOptions:
    out: CapacityReservationOptions = {}  # type: ignore[typeddict-item]
    child_usage_strategy = el.find("usageStrategy")
    if child_usage_strategy is not None:
        import capo_ec2.types.fleet_capacity_reservation_usage_strategy

        out["usage_strategy"] = (
            capo_ec2.types.fleet_capacity_reservation_usage_strategy.deserialize_ec2_query(
                child_usage_strategy
            )
        )
    return out
