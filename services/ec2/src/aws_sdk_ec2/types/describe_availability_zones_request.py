"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAvailabilityZonesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.zone_id_string_list
    import aws_sdk_ec2.types.zone_name_string_list


class DescribeAvailabilityZonesRequest(TypedDict):
    zone_names: NotRequired[
        "aws_sdk_ec2.types.zone_name_string_list.ZoneNameStringList"
    ]
    """<p>The names of the Availability Zones, Local Zones, and Wavelength Zones.</p>"""
    zone_ids: NotRequired["aws_sdk_ec2.types.zone_id_string_list.ZoneIdStringList"]
    """<p>The IDs of the Availability Zones, Local Zones, and Wavelength Zones.</p>"""
    all_availability_zones: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Include all Availability Zones, Local Zones, and Wavelength Zones regardless of your opt-in status.</p> <p>If you do not use this parameter, the results include only the zones for the Regions where you have chosen the option to opt in.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>group-long-name</code> - The long name of the zone group for the Availability Zone (for example, <code>US West (Oregon) 1</code>), the Local Zone (for example, for Zone group <code>us-west-2-lax-1</code>, it is <code>US West (Los Angeles)</code>, or the Wavelength Zone (for example, for Zone group <code>us-east-1-wl1</code>, it is <code>US East (Verizon)</code>.</p> </li> <li> <p> <code>group-name</code> - The name of the zone group for the Availability Zone (for example, <code>us-east-1-zg-1</code>), the Local Zone (for example, <code>us-west-2-lax-1</code>), or the Wavelength Zone (for example, <code>us-east-1-wl1</code>).</p> </li> <li> <p> <code>message</code> - The Zone message.</p> </li> <li> <p> <code>opt-in-status</code> - The opt-in status (<code>opted-in</code> | <code>not-opted-in</code> | <code>opt-in-not-required</code>).</p> </li> <li> <p> <code>parent-zone-id</code> - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.</p> </li> <li> <p> <code>parent-zone-name</code> - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.</p> </li> <li> <p> <code>region-name</code> - The name of the Region for the Zone (for example, <code>us-east-1</code>).</p> </li> <li> <p> <code>state</code> - The state of the Availability Zone, the Local Zone, or the Wavelength Zone (<code>available</code> | <code>unavailable</code> | <code>constrained</code>).</p> </li> <li> <p> <code>zone-id</code> - The ID of the Availability Zone (for example, <code>use1-az1</code>), the Local Zone (for example, <code>usw2-lax1-az1</code>), or the Wavelength Zone (for example, <code>us-east-1-wl1-bos-wlz-1</code>).</p> </li> <li> <p> <code>zone-name</code> - The name of the Availability Zone (for example, <code>us-east-1a</code>), the Local Zone (for example, <code>us-west-2-lax-1a</code>), or the Wavelength Zone (for example, <code>us-east-1-wl1-bos-wlz-1</code>).</p> </li> <li> <p> <code>zone-type</code> - The type of zone (<code>availability-zone</code> | <code>local-zone</code> | <code>wavelength-zone</code>).</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAvailabilityZonesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "zone_names" in value:
        import aws_sdk_ec2.types.zone_name_string_list

        aws_sdk_ec2.types.zone_name_string_list.serialize_ec2_query(
            value["zone_names"], pairs, f"{prefix}.ZoneNames"
        )
    if "zone_ids" in value:
        import aws_sdk_ec2.types.zone_id_string_list

        aws_sdk_ec2.types.zone_id_string_list.serialize_ec2_query(
            value["zone_ids"], pairs, f"{prefix}.ZoneIds"
        )
    if "all_availability_zones" in value:
        pairs.append(
            (
                f"{prefix}.AllAvailabilityZones",
                "true" if value["all_availability_zones"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribeAvailabilityZonesRequest:
    out: DescribeAvailabilityZonesRequest = {}  # type: ignore[typeddict-item]
    if el.find("ZoneNames") is not None:
        import aws_sdk_ec2.types.zone_name_string_list

        out["zone_names"] = (
            aws_sdk_ec2.types.zone_name_string_list.deserialize_ec2_query(
                el, "ZoneNames"
            )
        )
    if el.find("ZoneIds") is not None:
        import aws_sdk_ec2.types.zone_id_string_list

        out["zone_ids"] = aws_sdk_ec2.types.zone_id_string_list.deserialize_ec2_query(
            el, "ZoneIds"
        )
    child_all_availability_zones = el.find("AllAvailabilityZones")
    if child_all_availability_zones is not None:
        out["all_availability_zones"] = (
            child_all_availability_zones.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out
