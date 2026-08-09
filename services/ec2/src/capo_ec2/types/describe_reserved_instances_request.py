"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.offering_class_type
    import capo_ec2.types.offering_type_values
    import capo_ec2.types.reserved_instances_id_string_list


class DescribeReservedInstancesRequest(TypedDict, closed=True):
    offering_class: NotRequired["capo_ec2.types.offering_class_type.OfferingClassType"]
    """<p>Describes whether the Reserved Instance is Standard or Convertible.</p>"""
    reserved_instances_ids: NotRequired[
        "capo_ec2.types.reserved_instances_id_string_list.ReservedInstancesIdStringList"
    ]
    """<p>One or more Reserved Instance IDs.</p> <p>Default: Describes all your Reserved Instances, or only those otherwise specified.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>duration</code> - The duration of the Reserved Instance (one year or three years), in seconds (<code>31536000</code> | <code>94608000</code>).</p> </li> <li> <p> <code>end</code> - The time when the Reserved Instance expires (for example, 2015-08-07T11:54:42.000Z).</p> </li> <li> <p> <code>fixed-price</code> - The purchase price of the Reserved Instance (for example, 9800.0).</p> </li> <li> <p> <code>instance-type</code> - The instance type that is covered by the reservation.</p> </li> <li> <p> <code>scope</code> - The scope of the Reserved Instance (<code>Region</code> or <code>Availability Zone</code>).</p> </li> <li> <p> <code>product-description</code> - The Reserved Instance product platform description (<code>Linux/UNIX</code> | <code>Linux with SQL Server Standard</code> | <code>Linux with SQL Server Web</code> | <code>Linux with SQL Server Enterprise</code> | <code>SUSE Linux</code> | <code>Red Hat Enterprise Linux</code> | <code>Red Hat Enterprise Linux with HA</code> | <code>Windows</code> | <code>Windows with SQL Server Standard</code> | <code>Windows with SQL Server Web</code> | <code>Windows with SQL Server Enterprise</code>).</p> </li> <li> <p> <code>reserved-instances-id</code> - The ID of the Reserved Instance.</p> </li> <li> <p> <code>start</code> - The time at which the Reserved Instance purchase request was placed (for example, 2014-08-07T11:54:42.000Z).</p> </li> <li> <p> <code>state</code> - The state of the Reserved Instance (<code>payment-pending</code> | <code>active</code> | <code>payment-failed</code> | <code>retired</code>).</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>usage-price</code> - The usage price of the Reserved Instance, per hour (for example, 0.84).</p> </li> </ul>"""
    offering_type: NotRequired["capo_ec2.types.offering_type_values.OfferingTypeValues"]
    """<p>The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the <code>Medium Utilization</code> Reserved Instance offering type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "offering_class" in value:
        import capo_ec2.types.offering_class_type

        capo_ec2.types.offering_class_type.serialize_ec2_query(
            value["offering_class"], pairs, f"{key_prefix}OfferingClass"
        )
    if "reserved_instances_ids" in value:
        import capo_ec2.types.reserved_instances_id_string_list

        capo_ec2.types.reserved_instances_id_string_list.serialize_ec2_query(
            value["reserved_instances_ids"], pairs, f"{key_prefix}ReservedInstancesId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "offering_type" in value:
        import capo_ec2.types.offering_type_values

        capo_ec2.types.offering_type_values.serialize_ec2_query(
            value["offering_type"], pairs, f"{key_prefix}OfferingType"
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesRequest:
    out: DescribeReservedInstancesRequest = {}  # type: ignore[typeddict-item]
    child_offering_class = el.find("OfferingClass")
    if child_offering_class is not None:
        import capo_ec2.types.offering_class_type

        out["offering_class"] = (
            capo_ec2.types.offering_class_type.deserialize_ec2_query(
                child_offering_class
            )
        )
    child_reserved_instances_ids = el.find("ReservedInstancesId")
    if child_reserved_instances_ids is not None:
        import capo_ec2.types.reserved_instances_id_string_list

        out["reserved_instances_ids"] = (
            capo_ec2.types.reserved_instances_id_string_list.deserialize_ec2_query(
                child_reserved_instances_ids
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_offering_type = el.find("offeringType")
    if child_offering_type is not None:
        import capo_ec2.types.offering_type_values

        out["offering_type"] = (
            capo_ec2.types.offering_type_values.deserialize_ec2_query(
                child_offering_type
            )
        )
    return out
