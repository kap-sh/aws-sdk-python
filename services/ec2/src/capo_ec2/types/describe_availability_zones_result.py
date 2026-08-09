"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAvailabilityZonesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_list


class DescribeAvailabilityZonesResult(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_ec2.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>Information about the Availability Zones, Local Zones, and Wavelength Zones.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAvailabilityZonesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_ec2.types.availability_zone_list

        capo_ec2.types.availability_zone_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZoneInfo"
        )


def deserialize_ec2_query(el: Element) -> DescribeAvailabilityZonesResult:
    out: DescribeAvailabilityZonesResult = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("availabilityZoneInfo")
    if child_availability_zones is not None:
        import capo_ec2.types.availability_zone_list

        out["availability_zones"] = (
            capo_ec2.types.availability_zone_list.deserialize_ec2_query(
                child_availability_zones
            )
        )
    return out
