"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstances``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.date_time
    import capo_ec2.types.float
    import capo_ec2.types.instance_type
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.offering_class_type
    import capo_ec2.types.offering_type_values
    import capo_ec2.types.recurring_charges_list
    import capo_ec2.types.reserved_instance_state
    import capo_ec2.types.ri_product_description
    import capo_ec2.types.scope
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.tenancy


class ReservedInstances(TypedDict, closed=True):
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency of the Reserved Instance. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is <code>USD</code>.</p>"""
    instance_tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance.</p>"""
    offering_class: NotRequired["capo_ec2.types.offering_class_type.OfferingClassType"]
    """<p>The offering class of the Reserved Instance.</p>"""
    offering_type: NotRequired["capo_ec2.types.offering_type_values.OfferingTypeValues"]
    """<p>The Reserved Instance offering type.</p>"""
    recurring_charges: NotRequired[
        "capo_ec2.types.recurring_charges_list.RecurringChargesList"
    ]
    """<p>The recurring charge tag assigned to the resource.</p>"""
    scope: NotRequired["capo_ec2.types.scope.scope"]
    """<p>The scope of the Reserved Instance.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    reserved_instances_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type on which the Reserved Instance can be used.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p>"""
    start: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time the Reserved Instance started.</p>"""
    end: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time when the Reserved Instance expires.</p>"""
    duration: NotRequired["capo_ec2.types.long.Long"]
    """<p>The duration of the Reserved Instance, in seconds.</p>"""
    usage_price: NotRequired["capo_ec2.types.float.Float"]
    """<p>The usage price of the Reserved Instance, per hour.</p>"""
    fixed_price: NotRequired["capo_ec2.types.float.Float"]
    """<p>The purchase price of the Reserved Instance.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of reservations purchased.</p>"""
    product_description: NotRequired[
        "capo_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description.</p>"""
    state: NotRequired["capo_ec2.types.reserved_instance_state.ReservedInstanceState"]
    """<p>The state of the Reserved Instance purchase.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "currency_code" in value:
        import capo_ec2.types.currency_code_values

        capo_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{key_prefix}CurrencyCode"
        )
    if "instance_tenancy" in value:
        import capo_ec2.types.tenancy

        capo_ec2.types.tenancy.serialize_ec2_query(
            value["instance_tenancy"], pairs, f"{key_prefix}InstanceTenancy"
        )
    if "offering_class" in value:
        import capo_ec2.types.offering_class_type

        capo_ec2.types.offering_class_type.serialize_ec2_query(
            value["offering_class"], pairs, f"{key_prefix}OfferingClass"
        )
    if "offering_type" in value:
        import capo_ec2.types.offering_type_values

        capo_ec2.types.offering_type_values.serialize_ec2_query(
            value["offering_type"], pairs, f"{key_prefix}OfferingType"
        )
    if "recurring_charges" in value:
        import capo_ec2.types.recurring_charges_list

        capo_ec2.types.recurring_charges_list.serialize_ec2_query(
            value["recurring_charges"], pairs, f"{key_prefix}RecurringCharges"
        )
    if "scope" in value:
        import capo_ec2.types.scope

        capo_ec2.types.scope.serialize_ec2_query(
            value["scope"], pairs, f"{key_prefix}Scope"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "reserved_instances_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedInstancesId", str(value["reserved_instances_id"]))
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "start" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start"], pairs, f"{key_prefix}Start"
        )
    if "end" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end"], pairs, f"{key_prefix}End"
        )
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "usage_price" in value:
        pairs.append(
            (
                f"{key_prefix}UsagePrice",
                (
                    "NaN"
                    if value["usage_price"] != value["usage_price"]
                    else "Infinity"
                    if value["usage_price"] == float("inf")
                    else "-Infinity"
                    if value["usage_price"] == float("-inf")
                    else str(value["usage_price"])
                ),
            )
        )
    if "fixed_price" in value:
        pairs.append(
            (
                f"{key_prefix}FixedPrice",
                (
                    "NaN"
                    if value["fixed_price"] != value["fixed_price"]
                    else "Infinity"
                    if value["fixed_price"] == float("inf")
                    else "-Infinity"
                    if value["fixed_price"] == float("-inf")
                    else str(value["fixed_price"])
                ),
            )
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "product_description" in value:
        import capo_ec2.types.ri_product_description

        capo_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{key_prefix}ProductDescription"
        )
    if "state" in value:
        import capo_ec2.types.reserved_instance_state

        capo_ec2.types.reserved_instance_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstances:
    out: ReservedInstances = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("currencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_instance_tenancy = el.find("instanceTenancy")
    if child_instance_tenancy is not None:
        import capo_ec2.types.tenancy

        out["instance_tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_offering_class = el.find("offeringClass")
    if child_offering_class is not None:
        import capo_ec2.types.offering_class_type

        out["offering_class"] = (
            capo_ec2.types.offering_class_type.deserialize_ec2_query(
                child_offering_class
            )
        )
    child_offering_type = el.find("offeringType")
    if child_offering_type is not None:
        import capo_ec2.types.offering_type_values

        out["offering_type"] = (
            capo_ec2.types.offering_type_values.deserialize_ec2_query(
                child_offering_type
            )
        )
    child_recurring_charges = el.find("recurringCharges")
    if child_recurring_charges is not None:
        import capo_ec2.types.recurring_charges_list

        out["recurring_charges"] = (
            capo_ec2.types.recurring_charges_list.deserialize_ec2_query(
                child_recurring_charges
            )
        )
    child_scope = el.find("scope")
    if child_scope is not None:
        import capo_ec2.types.scope

        out["scope"] = capo_ec2.types.scope.deserialize_ec2_query(child_scope)
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_reserved_instances_id = el.find("reservedInstancesId")
    if child_reserved_instances_id is not None:
        out["reserved_instances_id"] = str(child_reserved_instances_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_start = el.find("start")
    if child_start is not None:
        import capo_ec2.types.date_time

        out["start"] = capo_ec2.types.date_time.deserialize_ec2_query(child_start)
    child_end = el.find("end")
    if child_end is not None:
        import capo_ec2.types.date_time

        out["end"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end)
    child_duration = el.find("duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_usage_price = el.find("usagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_fixed_price = el.find("fixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_product_description = el.find("productDescription")
    if child_product_description is not None:
        import capo_ec2.types.ri_product_description

        out["product_description"] = (
            capo_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.reserved_instance_state

        out["state"] = capo_ec2.types.reserved_instance_state.deserialize_ec2_query(
            child_state
        )
    return out
