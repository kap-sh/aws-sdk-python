"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AddAvailabilityZonesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.availability_zones


class AddAvailabilityZonesOutput(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_elastic_load_balancing.types.availability_zones.AvailabilityZones"
    ]
    """<p>The updated list of Availability Zones for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddAvailabilityZonesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_elastic_load_balancing.types.availability_zones

        capo_elastic_load_balancing.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )


def deserialize_query(el: Element) -> AddAvailabilityZonesOutput:
    out: AddAvailabilityZonesOutput = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_elastic_load_balancing.types.availability_zones

        out["availability_zones"] = (
            capo_elastic_load_balancing.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    return out
