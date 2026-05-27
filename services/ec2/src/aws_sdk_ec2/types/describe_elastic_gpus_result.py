"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeElasticGpusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_set
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeElasticGpusResult(TypedDict):
    elastic_gpu_set: NotRequired["aws_sdk_ec2.types.elastic_gpu_set.ElasticGpuSet"]
    """<p>Information about the Elastic Graphics accelerators.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of items to return. If the total number of items available is more than the value specified in max-items then a Next-Token will be provided in the output that you can use to resume pagination.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
