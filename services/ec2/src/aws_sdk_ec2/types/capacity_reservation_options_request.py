"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy


class CapacityReservationOptionsRequest(TypedDict):
    usage_strategy: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy.FleetCapacityReservationUsageStrategy"
    ]
    """<p>Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.</p> <p>If you specify <code>use-capacity-reservations-first</code>, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (<code>lowest-price</code> or <code>prioritized</code>) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (<code>lowest-price</code> or <code>prioritized</code>).</p> <p>If you do not specify a value, the fleet fulfils the On-Demand capacity according to the chosen On-Demand allocation strategy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "usage_strategy" in value:
        import aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy

        aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy.serialize_ec2_query(
            value["usage_strategy"], pairs, f"{prefix}.UsageStrategy"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationOptionsRequest:
    out: CapacityReservationOptionsRequest = {}  # type: ignore[typeddict-item]
    child_usage_strategy = el.find("UsageStrategy")
    if child_usage_strategy is not None:
        import aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy

        out["usage_strategy"] = (
            aws_sdk_ec2.types.fleet_capacity_reservation_usage_strategy.deserialize_ec2_query(
                child_usage_strategy
            )
        )
    return out
