"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_gpu_id
    import aws_sdk_ec2.types.string


class ElasticGpuAssociation(TypedDict):
    elastic_gpu_id: NotRequired["aws_sdk_ec2.types.elastic_gpu_id.ElasticGpuId"]
    """<p>The ID of the Elastic Graphics accelerator.</p>"""
    elastic_gpu_association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    elastic_gpu_association_state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the association between the instance and the Elastic Graphics accelerator.</p>"""
    elastic_gpu_association_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The time the Elastic Graphics accelerator was associated with the instance.</p>"""
