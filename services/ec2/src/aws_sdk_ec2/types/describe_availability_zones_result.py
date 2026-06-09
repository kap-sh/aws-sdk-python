"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAvailabilityZonesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_list


class DescribeAvailabilityZonesResult(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>Information about the Availability Zones, Local Zones, and Wavelength Zones.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAvailabilityZonesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zones" in value:
        import aws_sdk_ec2.types.availability_zone_list

        aws_sdk_ec2.types.availability_zone_list.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZoneInfo"
        )


def deserialize_ec2_query(el: Element) -> DescribeAvailabilityZonesResult:
    out: DescribeAvailabilityZonesResult = {}  # type: ignore[typeddict-item]
    if el.find("AvailabilityZoneInfo") is not None:
        import aws_sdk_ec2.types.availability_zone_list

        out["availability_zones"] = (
            aws_sdk_ec2.types.availability_zone_list.deserialize_ec2_query(
                el, "AvailabilityZoneInfo"
            )
        )
    return out
