"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CrossZoneLoadBalancing``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing_enabled


class CrossZoneLoadBalancing(TypedDict, closed=True):
    enabled: "aws_sdk_elastic_load_balancing.types.cross_zone_load_balancing_enabled.CrossZoneLoadBalancingEnabled"
    """<p>Specifies whether cross-zone load balancing is enabled for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CrossZoneLoadBalancing, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.Enabled", "true" if value.get("enabled", False) else "false")
    )


def deserialize_query(el: Element) -> CrossZoneLoadBalancing:
    out: CrossZoneLoadBalancing = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    return out
