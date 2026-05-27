"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeElasticGpusRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_elastic_gpus_max_results
    import aws_sdk_ec2.types.elastic_gpu_id_set
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeElasticGpusRequest(TypedDict):
    elastic_gpu_ids: NotRequired["aws_sdk_ec2.types.elastic_gpu_id_set.ElasticGpuIdSet"]
    """<p>The Elastic Graphics accelerator IDs.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone in which the Elastic Graphics accelerator resides.</p> </li> <li> <p> <code>elastic-gpu-health</code> - The status of the Elastic Graphics accelerator (<code>OK</code> | <code>IMPAIRED</code>).</p> </li> <li> <p> <code>elastic-gpu-state</code> - The state of the Elastic Graphics accelerator (<code>ATTACHED</code>).</p> </li> <li> <p> <code>elastic-gpu-type</code> - The type of Elastic Graphics accelerator; for example, <code>eg1.medium</code>.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance to which the Elastic Graphics accelerator is associated.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_elastic_gpus_max_results.DescribeElasticGpusMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 5 and 1000.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""
