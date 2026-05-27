"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstances``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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


class ReservedInstances(TypedDict):
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
