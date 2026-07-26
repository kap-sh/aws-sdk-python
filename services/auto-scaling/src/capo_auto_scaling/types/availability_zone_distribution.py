"""Generated from Smithy shape ``com.amazonaws.autoscaling#AvailabilityZoneDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.capacity_distribution_strategy


class AvailabilityZoneDistribution(TypedDict, closed=True):
    capacity_distribution_strategy: NotRequired[
        "capo_auto_scaling.types.capacity_distribution_strategy.CapacityDistributionStrategy"
    ]
    """<p> If launches fail in an Availability Zone, the following strategies are available. The default is <code>balanced-best-effort</code>. </p> <ul> <li> <p> <code>balanced-only</code> - If launches fail in an Availability Zone, Auto Scaling will continue to attempt to launch in the unhealthy zone to preserve a balanced distribution.</p> </li> <li> <p> <code>balanced-best-effort</code> - If launches fail in an Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone instead.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZoneDistribution, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_distribution_strategy" in value:
        import capo_auto_scaling.types.capacity_distribution_strategy

        capo_auto_scaling.types.capacity_distribution_strategy.serialize_query(
            value["capacity_distribution_strategy"],
            pairs,
            f"{prefix}.CapacityDistributionStrategy",
        )


def deserialize_query(el: Element) -> AvailabilityZoneDistribution:
    out: AvailabilityZoneDistribution = {}  # type: ignore[typeddict-item]
    child_capacity_distribution_strategy = el.find("CapacityDistributionStrategy")
    if child_capacity_distribution_strategy is not None:
        import capo_auto_scaling.types.capacity_distribution_strategy

        out["capacity_distribution_strategy"] = (
            capo_auto_scaling.types.capacity_distribution_strategy.deserialize_query(
                child_capacity_distribution_strategy
            )
        )
    return out
