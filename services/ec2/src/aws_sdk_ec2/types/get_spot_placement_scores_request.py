"""Generated from Smithy shape ``com.amazonaws.ec2#GetSpotPlacementScoresRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_requirements_with_metadata_request
    import aws_sdk_ec2.types.instance_types
    import aws_sdk_ec2.types.region_names
    import aws_sdk_ec2.types.spot_placement_scores_max_results
    import aws_sdk_ec2.types.spot_placement_scores_target_capacity
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.target_capacity_unit_type


class GetSpotPlacementScoresRequest(TypedDict):
    instance_types: NotRequired["aws_sdk_ec2.types.instance_types.InstanceTypes"]
    """<p>The instance types. We recommend that you specify at least three instance types. If you specify one or two instance types, or specify variations of a single instance type (for example, an <code>m3.xlarge</code> with and without instance storage), the returned placement score will always be low. </p> <p>If you specify <code>InstanceTypes</code>, you can't specify <code>InstanceRequirementsWithMetadata</code>.</p>"""
    target_capacity: NotRequired[
        "aws_sdk_ec2.types.spot_placement_scores_target_capacity.SpotPlacementScoresTargetCapacity"
    ]
    """<p>The target capacity.</p>"""
    target_capacity_unit_type: NotRequired[
        "aws_sdk_ec2.types.target_capacity_unit_type.TargetCapacityUnitType"
    ]
    """<p>The unit for the target capacity.</p>"""
    single_availability_zone: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> so that the response returns a list of scored Availability Zones. Otherwise, the response returns a list of scored Regions.</p> <p>A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone.</p>"""
    region_names: NotRequired["aws_sdk_ec2.types.region_names.RegionNames"]
    """<p>The Regions used to narrow down the list of Regions to be scored. Enter the Region code, for example, <code>us-east-1</code>.</p>"""
    instance_requirements_with_metadata: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_with_metadata_request.InstanceRequirementsWithMetadataRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <p>If you specify <code>InstanceRequirementsWithMetadata</code>, you can't specify <code>InstanceTypes</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.spot_placement_scores_max_results.SpotPlacementScoresMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
