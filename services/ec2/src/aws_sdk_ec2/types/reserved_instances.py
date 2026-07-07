"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstances``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.float
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.offering_class_type
    import aws_sdk_ec2.types.offering_type_values
    import aws_sdk_ec2.types.recurring_charges_list
    import aws_sdk_ec2.types.reserved_instance_state
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.scope
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tenancy


class ReservedInstances(TypedDict, closed=True):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency of the Reserved Instance. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is <code>USD</code>.</p>"""
    instance_tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance.</p>"""
    offering_class: NotRequired[
        "aws_sdk_ec2.types.offering_class_type.OfferingClassType"
    ]
    """<p>The offering class of the Reserved Instance.</p>"""
    offering_type: NotRequired[
        "aws_sdk_ec2.types.offering_type_values.OfferingTypeValues"
    ]
    """<p>The Reserved Instance offering type.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_ec2.types.recurring_charges_list.RecurringChargesList"
    ]
    """<p>The recurring charge tag assigned to the resource.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.scope.scope"]
    """<p>The scope of the Reserved Instance.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type on which the Reserved Instance can be used.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p>"""
    start: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the Reserved Instance started.</p>"""
    end: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time when the Reserved Instance expires.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The duration of the Reserved Instance, in seconds.</p>"""
    usage_price: NotRequired["aws_sdk_ec2.types.float.Float"]
    """<p>The usage price of the Reserved Instance, per hour.</p>"""
    fixed_price: NotRequired["aws_sdk_ec2.types.float.Float"]
    """<p>The purchase price of the Reserved Instance.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of reservations purchased.</p>"""
    product_description: NotRequired[
        "aws_sdk_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.reserved_instance_state.ReservedInstanceState"
    ]
    """<p>The state of the Reserved Instance purchase.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )
    if "instance_tenancy" in value:
        import aws_sdk_ec2.types.tenancy

        aws_sdk_ec2.types.tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{prefix}.InstanceTenancy"
        )
    if "offering_class" in value:
        import aws_sdk_ec2.types.offering_class_type

        aws_sdk_ec2.types.offering_class_type.serialize_ec2_query(
            value["offering_class"], pairs, f"{prefix}.OfferingClass"
        )
    if "offering_type" in value:
        import aws_sdk_ec2.types.offering_type_values

        aws_sdk_ec2.types.offering_type_values.serialize_ec2_query(
            value["offering_type"], pairs, f"{prefix}.OfferingType"
        )
    if "recurring_charges" in value:
        import aws_sdk_ec2.types.recurring_charges_list

        aws_sdk_ec2.types.recurring_charges_list.serialize_ec2_query(
            value["recurring_charges"], pairs, f"{prefix}.RecurringCharges"
        )
    if "scope" in value:
        import aws_sdk_ec2.types.scope

        aws_sdk_ec2.types.scope.serialize_ec2_query(
            value["scope"], pairs, f"{prefix}.Scope"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{prefix}.ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "start" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["start"], pairs, f"{prefix}.Start"
        )
    if "end" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["end"], pairs, f"{prefix}.End"
        )
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "usage_price" in value:
        pairs.append((f"{prefix}.UsagePrice", str(value["usage_price"])))
    if "fixed_price" in value:
        pairs.append((f"{prefix}.FixedPrice", str(value["fixed_price"])))
    if "instance_count" in value:
        pairs.append((f"{prefix}.InstanceCount", str(value["instance_count"])))
    if "product_description" in value:
        import aws_sdk_ec2.types.ri_product_description

        aws_sdk_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{prefix}.ProductDescription"
        )
    if "state" in value:
        import aws_sdk_ec2.types.reserved_instance_state

        aws_sdk_ec2.types.reserved_instance_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstances:
    out: ReservedInstances = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_instance_tenancy = el.find("InstanceTenancy")
    if child_instance_tenancy is not None:
        import aws_sdk_ec2.types.tenancy

        out["instance_tenancy"] = aws_sdk_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_offering_class = el.find("OfferingClass")
    if child_offering_class is not None:
        import aws_sdk_ec2.types.offering_class_type

        out["offering_class"] = (
            aws_sdk_ec2.types.offering_class_type.deserialize_ec2_query(
                child_offering_class
            )
        )
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        import aws_sdk_ec2.types.offering_type_values

        out["offering_type"] = (
            aws_sdk_ec2.types.offering_type_values.deserialize_ec2_query(
                child_offering_type
            )
        )
    if el.find("RecurringCharges") is not None:
        import aws_sdk_ec2.types.recurring_charges_list

        out["recurring_charges"] = (
            aws_sdk_ec2.types.recurring_charges_list.deserialize_ec2_query(
                el, "RecurringCharges"
            )
        )
    child_scope = el.find("Scope")
    if child_scope is not None:
        import aws_sdk_ec2.types.scope

        out["scope"] = aws_sdk_ec2.types.scope.deserialize_ec2_query(child_scope)
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_reserved_instances_id = el.find("ReservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_start = el.find("Start")
    if child_start is not None:
        import aws_sdk_ec2.types.date_time

        out["start"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(child_start)
    child_end = el.find("End")
    if child_end is not None:
        import aws_sdk_ec2.types.date_time

        out["end"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(child_end)
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_usage_price = el.find("UsagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_fixed_price = el.find("FixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        import aws_sdk_ec2.types.ri_product_description

        out["product_description"] = (
            aws_sdk_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.reserved_instance_state

        out["state"] = aws_sdk_ec2.types.reserved_instance_state.deserialize_ec2_query(
            child_state
        )
    return out
