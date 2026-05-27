"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesOffering``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.float
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.offering_class_type
    import aws_sdk_ec2.types.offering_type_values
    import aws_sdk_ec2.types.pricing_details_list
    import aws_sdk_ec2.types.recurring_charges_list
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.scope
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class ReservedInstancesOffering(TypedDict):
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency of the Reserved Instance offering you are purchasing. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is <code>USD</code>.</p>"""
    instance_tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance.</p>"""
    marketplace: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the offering is available through the Reserved Instance Marketplace (resale) or Amazon Web Services. If it's a Reserved Instance Marketplace offering, this is <code>true</code>.</p>"""
    offering_class: NotRequired[
        "aws_sdk_ec2.types.offering_class_type.OfferingClassType"
    ]
    """<p>If <code>convertible</code> it can be exchanged for Reserved Instances of the same or higher monetary value, with different configurations. If <code>standard</code>, it is not possible to perform an exchange.</p>"""
    offering_type: NotRequired[
        "aws_sdk_ec2.types.offering_type_values.OfferingTypeValues"
    ]
    """<p>The Reserved Instance offering type.</p>"""
    pricing_details: NotRequired[
        "aws_sdk_ec2.types.pricing_details_list.PricingDetailsList"
    ]
    """<p>The pricing details of the Reserved Instance offering.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_ec2.types.recurring_charges_list.RecurringChargesList"
    ]
    """<p>The recurring charge tag assigned to the resource.</p>"""
    scope: NotRequired["aws_sdk_ec2.types.scope.scope"]
    """<p>Whether the Reserved Instance is applied to instances in a Region or an Availability Zone.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p>"""
    reserved_instances_offering_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Reserved Instance offering. This is the offering ID used in <a>GetReservedInstancesExchangeQuote</a> to confirm that an exchange can be made.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type on which the Reserved Instance can be used.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p>"""
    duration: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The duration of the Reserved Instance, in seconds.</p>"""
    usage_price: NotRequired["aws_sdk_ec2.types.float.Float"]
    """<p>The usage price of the Reserved Instance, per hour.</p>"""
    fixed_price: NotRequired["aws_sdk_ec2.types.float.Float"]
    """<p>The purchase price of the Reserved Instance.</p>"""
    product_description: NotRequired[
        "aws_sdk_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description.</p>"""
