"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AddAvailabilityZonesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.availability_zones


class AddAvailabilityZonesOutput(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_elastic_load_balancing.types.availability_zones.AvailabilityZones"
    ]
    """<p>The updated list of Availability Zones for the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddAvailabilityZonesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zones" in value:
        import aws_sdk_elastic_load_balancing.types.availability_zones

        aws_sdk_elastic_load_balancing.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )


def deserialize_query(el: Element) -> AddAvailabilityZonesOutput:
    out: AddAvailabilityZonesOutput = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import aws_sdk_elastic_load_balancing.types.availability_zones

        out["availability_zones"] = (
            aws_sdk_elastic_load_balancing.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    return out
