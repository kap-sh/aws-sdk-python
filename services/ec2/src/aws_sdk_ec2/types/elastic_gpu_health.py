"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuHealth``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_status


class ElasticGpuHealth(TypedDict):
    status: NotRequired["aws_sdk_ec2.types.elastic_gpu_status.ElasticGpuStatus"]
    """<p>The health status.</p>"""
