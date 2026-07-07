"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultSubnetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean


class CreateDefaultSubnetRequest(TypedDict, closed=True):
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone in which to create the default subnet.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipv6_native: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to create an IPv6 only subnet. If you already have a default subnet for this Availability Zone, you must delete it before you can create an IPv6 only subnet.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDefaultSubnetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipv6_native" in value:
        pairs.append(
            (f"{prefix}.Ipv6Native", "true" if value["ipv6_native"] else "false")
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> CreateDefaultSubnetRequest:
    out: CreateDefaultSubnetRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipv6_native = el.find("Ipv6Native")
    if child_ipv6_native is not None:
        out["ipv6_native"] = (child_ipv6_native.text or "").lower() == "true"
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
