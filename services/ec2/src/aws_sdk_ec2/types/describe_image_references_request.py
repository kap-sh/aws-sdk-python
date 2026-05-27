"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageReferencesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_image_references_image_id_string_list
    import aws_sdk_ec2.types.describe_image_references_max_results
    import aws_sdk_ec2.types.resource_type_request_list
    import aws_sdk_ec2.types.string


class DescribeImageReferencesRequest(TypedDict):
    image_ids: NotRequired[
        "aws_sdk_ec2.types.describe_image_references_image_id_string_list.DescribeImageReferencesImageIdStringList"
    ]
    """<p>The IDs of the images to check for resource references.</p>"""
    include_all_resource_types: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to check all supported Amazon Web Services resource types for image references. When specified, default values are applied for <code>ResourceTypeOptions</code>. For the default values, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-ami-references.html#how-ami-references-works\">How AMI reference checks work</a> in the <i>Amazon EC2 User Guide</i>. If you also specify <code>ResourceTypes</code> with <code>ResourceTypeOptions</code>, your specified values override the default values.</p> <p>Supported resource types: <code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code> | <code>ssm:Parameter</code> | <code>imagebuilder:ImageRecipe</code> | <code>imagebuilder:ContainerRecipe</code> </p> <p>Either <code>IncludeAllResourceTypes</code> or <code>ResourceTypes</code> must be specified.</p>"""
    resource_types: NotRequired[
        "aws_sdk_ec2.types.resource_type_request_list.ResourceTypeRequestList"
    ]
    """<p>The Amazon Web Services resource types to check for image references.</p> <p>Either <code>IncludeAllResourceTypes</code> or <code>ResourceTypes</code> must be specified.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_image_references_max_results.DescribeImageReferencesMaxResults"
    ]
    """<p> The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>. </p>"""
