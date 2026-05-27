"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_id_list
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeIamInstanceProfileAssociationsRequest(TypedDict):
    association_ids: NotRequired[
        "aws_sdk_ec2.types.association_id_list.AssociationIdList"
    ]
    """<p>The IAM instance profile associations.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>state</code> - The state of the association (<code>associating</code> | <code>associated</code> | <code>disassociating</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_iam_instance_profile_associations_max_results.DescribeIamInstanceProfileAssociationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
