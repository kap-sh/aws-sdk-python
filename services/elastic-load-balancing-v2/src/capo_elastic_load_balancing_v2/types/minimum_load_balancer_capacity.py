"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#MinimumLoadBalancerCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.capacity_units


class MinimumLoadBalancerCapacity(TypedDict, closed=True):
    capacity_units: NotRequired[
        "capo_elastic_load_balancing_v2.types.capacity_units.CapacityUnits"
    ]
    """<p>The number of capacity units.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MinimumLoadBalancerCapacity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_units" in value:
        pairs.append((f"{prefix}.CapacityUnits", str(value["capacity_units"])))


def deserialize_query(el: Element) -> MinimumLoadBalancerCapacity:
    out: MinimumLoadBalancerCapacity = {}  # type: ignore[typeddict-item]
    child_capacity_units = el.find("CapacityUnits")
    if child_capacity_units is not None:
        out["capacity_units"] = int(child_capacity_units.text or "")
    return out
