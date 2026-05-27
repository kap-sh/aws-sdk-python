"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_health
    import aws_sdk_ec2.types.elastic_gpu_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ElasticGpus(TypedDict):
    elastic_gpu_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Elastic Graphics accelerator.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in the which the Elastic Graphics accelerator resides.</p>"""
    elastic_gpu_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of Elastic Graphics accelerator.</p>"""
    elastic_gpu_health: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_health.ElasticGpuHealth"
    ]
    """<p>The status of the Elastic Graphics accelerator.</p>"""
    elastic_gpu_state: NotRequired[
        "aws_sdk_ec2.types.elastic_gpu_state.ElasticGpuState"
    ]
    """<p>The state of the Elastic Graphics accelerator.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance to which the Elastic Graphics accelerator is attached.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Elastic Graphics accelerator.</p>"""
