"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTypesFromInstanceRequirementsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_requirements_request
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.virtualization_type_set


class GetInstanceTypesFromInstanceRequirementsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    architecture_types: NotRequired[
        "aws_sdk_ec2.types.architecture_type_set.ArchitectureTypeSet"
    ]
    """<p>The processor architecture type.</p>"""
    virtualization_types: NotRequired[
        "aws_sdk_ec2.types.virtualization_type_set.VirtualizationTypeSet"
    ]
    """<p>The virtualization type.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes required for the instance types.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    context: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved.</p>"""
