"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.boolean
    import capo_ec2.types.currency_code_values
    import capo_ec2.types.float
    import capo_ec2.types.instance_type
    import capo_ec2.types.long
    import capo_ec2.types.offering_class_type
    import capo_ec2.types.offering_type_values
    import capo_ec2.types.pricing_details_list
    import capo_ec2.types.recurring_charges_list
    import capo_ec2.types.ri_product_description
    import capo_ec2.types.scope
    import capo_ec2.types.string
    import capo_ec2.types.tenancy


class ReservedInstancesOffering(TypedDict, closed=True):
    currency_code: NotRequired["capo_ec2.types.currency_code_values.CurrencyCodeValues"]
    """<p>The currency of the Reserved Instance offering you are purchasing. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is <code>USD</code>.</p>"""
    instance_tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance.</p>"""
    marketplace: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the offering is available through the Reserved Instance Marketplace (resale) or Amazon Web Services. If it's a Reserved Instance Marketplace offering, this is <code>true</code>.</p>"""
    offering_class: NotRequired["capo_ec2.types.offering_class_type.OfferingClassType"]
    """<p>If <code>convertible</code> it can be exchanged for Reserved Instances of the same or higher monetary value, with different configurations. If <code>standard</code>, it is not possible to perform an exchange.</p>"""
    offering_type: NotRequired["capo_ec2.types.offering_type_values.OfferingTypeValues"]
    """<p>The Reserved Instance offering type.</p>"""
    pricing_details: NotRequired[
        "capo_ec2.types.pricing_details_list.PricingDetailsList"
    ]
    """<p>The pricing details of the Reserved Instance offering.</p>"""
    recurring_charges: NotRequired[
        "capo_ec2.types.recurring_charges_list.RecurringChargesList"
    ]
    """<p>The recurring charge tag assigned to the resource.</p>"""
    scope: NotRequired["capo_ec2.types.scope.scope"]
    """<p>Whether the Reserved Instance is applied to instances in a Region or an Availability Zone.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p>"""
    reserved_instances_offering_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance offering. This is the offering ID used in <a>GetReservedInstancesExchangeQuote</a> to confirm that an exchange can be made.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type on which the Reserved Instance can be used.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p>"""
    duration: NotRequired["capo_ec2.types.long.Long"]
    """<p>The duration of the Reserved Instance, in seconds.</p>"""
    usage_price: NotRequired["capo_ec2.types.float.Float"]
    """<p>The usage price of the Reserved Instance, per hour.</p>"""
    fixed_price: NotRequired["capo_ec2.types.float.Float"]
    """<p>The purchase price of the Reserved Instance.</p>"""
    product_description: NotRequired[
        "capo_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesOffering, pairs: list[tuple[str, str]], prefix: str
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
    if "marketplace" in value:
        pairs.append(
            (f"{key_prefix}Marketplace", "true" if value["marketplace"] else "false")
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
    if "pricing_details" in value:
        import capo_ec2.types.pricing_details_list

        capo_ec2.types.pricing_details_list.serialize_ec2_query(
            value["pricing_details"], pairs, f"{key_prefix}PricingDetailsSet"
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
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "reserved_instances_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedInstancesOfferingId",
                str(value["reserved_instances_offering_id"]),
            )
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "usage_price" in value:
        pairs.append((f"{key_prefix}UsagePrice", str(value["usage_price"])))
    if "fixed_price" in value:
        pairs.append((f"{key_prefix}FixedPrice", str(value["fixed_price"])))
    if "product_description" in value:
        import capo_ec2.types.ri_product_description

        capo_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{key_prefix}ProductDescription"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesOffering:
    out: ReservedInstancesOffering = {}  # type: ignore[typeddict-item]
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import capo_ec2.types.currency_code_values

        out["currency_code"] = (
            capo_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_instance_tenancy = el.find("InstanceTenancy")
    if child_instance_tenancy is not None:
        import capo_ec2.types.tenancy

        out["instance_tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(
            child_instance_tenancy
        )
    child_marketplace = el.find("Marketplace")
    if child_marketplace is not None:
        out["marketplace"] = (child_marketplace.text or "").lower() == "true"
    child_offering_class = el.find("OfferingClass")
    if child_offering_class is not None:
        import capo_ec2.types.offering_class_type

        out["offering_class"] = (
            capo_ec2.types.offering_class_type.deserialize_ec2_query(
                child_offering_class
            )
        )
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        import capo_ec2.types.offering_type_values

        out["offering_type"] = (
            capo_ec2.types.offering_type_values.deserialize_ec2_query(
                child_offering_type
            )
        )
    if el.find("PricingDetailsSet") is not None:
        import capo_ec2.types.pricing_details_list

        out["pricing_details"] = (
            capo_ec2.types.pricing_details_list.deserialize_ec2_query(
                el, "PricingDetailsSet"
            )
        )
    if el.find("RecurringCharges") is not None:
        import capo_ec2.types.recurring_charges_list

        out["recurring_charges"] = (
            capo_ec2.types.recurring_charges_list.deserialize_ec2_query(
                el, "RecurringCharges"
            )
        )
    child_scope = el.find("Scope")
    if child_scope is not None:
        import capo_ec2.types.scope

        out["scope"] = capo_ec2.types.scope.deserialize_ec2_query(child_scope)
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_reserved_instances_offering_id = el.find("ReservedInstancesOfferingId")
    if child_reserved_instances_offering_id is not None:
        out["reserved_instances_offering_id"] = str(
            child_reserved_instances_offering_id.text or ""
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_usage_price = el.find("UsagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_fixed_price = el.find("FixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        import capo_ec2.types.ri_product_description

        out["product_description"] = (
            capo_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    return out
