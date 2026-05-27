"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.offering_class_type
    import aws_sdk_ec2.types.offering_type_values
    import aws_sdk_ec2.types.reserved_instances_offering_id_string_list
    import aws_sdk_ec2.types.ri_product_description
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class DescribeReservedInstancesOfferingsRequest(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Reserved Instance can be used.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both.</p>"""
    include_marketplace: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Include Reserved Instance Marketplace offerings in the response.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type that the reservation will cover (for example, <code>m1.small</code>). For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Amazon EC2 instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    max_duration: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The maximum duration (in seconds) to filter when searching for offerings.</p> <p>Default: 94608000 (3 years)</p>"""
    max_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances to filter when searching for offerings.</p> <p>Default: 20</p>"""
    min_duration: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The minimum duration (in seconds) to filter when searching for offerings.</p> <p>Default: 2592000 (1 month)</p>"""
    offering_class: NotRequired[
        "aws_sdk_ec2.types.offering_class_type.OfferingClassType"
    ]
    """<p>The offering class of the Reserved Instance. Can be <code>standard</code> or <code>convertible</code>.</p>"""
    product_description: NotRequired[
        "aws_sdk_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The Reserved Instance product platform description. Instances that include <code>(Amazon VPC)</code> in the description are for use with Amazon VPC.</p>"""
    reserved_instances_offering_ids: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_id_string_list.ReservedInstancesOfferingIdStringList"
    ]
    """<p>One or more Reserved Instances offering IDs.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone where the Reserved Instance can be used.</p> </li> <li> <p> <code>duration</code> - The duration of the Reserved Instance (for example, one year or three years), in seconds (<code>31536000</code> | <code>94608000</code>).</p> </li> <li> <p> <code>fixed-price</code> - The purchase price of the Reserved Instance (for example, 9800.0).</p> </li> <li> <p> <code>instance-type</code> - The instance type that is covered by the reservation.</p> </li> <li> <p> <code>marketplace</code> - Set to <code>true</code> to show only Reserved Instance Marketplace offerings. When this filter is not used, which is the default behavior, all offerings from both Amazon Web Services and the Reserved Instance Marketplace are listed.</p> </li> <li> <p> <code>product-description</code> - The Reserved Instance product platform description (<code>Linux/UNIX</code> | <code>Linux with SQL Server Standard</code> | <code>Linux with SQL Server Web</code> | <code>Linux with SQL Server Enterprise</code> | <code>SUSE Linux</code> | <code>Red Hat Enterprise Linux</code> | <code>Red Hat Enterprise Linux with HA</code> | <code>Windows</code> | <code>Windows with SQL Server Standard</code> | <code>Windows with SQL Server Web</code> | <code>Windows with SQL Server Enterprise</code>).</p> </li> <li> <p> <code>reserved-instances-offering-id</code> - The Reserved Instances offering ID.</p> </li> <li> <p> <code>scope</code> - The scope of the Reserved Instance (<code>Availability Zone</code> or <code>Region</code>).</p> </li> <li> <p> <code>usage-price</code> - The usage price of the Reserved Instance, per hour (for example, 0.84).</p> </li> </ul>"""
    instance_tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instances covered by the reservation. A Reserved Instance with a tenancy of <code>dedicated</code> is applied to instances that run in a VPC on single-tenant hardware (i.e., Dedicated Instances).</p> <p> <b>Important:</b> The <code>host</code> value cannot be used with this parameter. Use the <code>default</code> or <code>dedicated</code> values only.</p> <p>Default: <code>default</code> </p>"""
    offering_type: NotRequired[
        "aws_sdk_ec2.types.offering_type_values.OfferingTypeValues"
    ]
    """<p>The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the <code>Medium Utilization</code> Reserved Instance offering type. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned <code>NextToken</code> value. The maximum is 100.</p> <p>Default: 100</p>"""
