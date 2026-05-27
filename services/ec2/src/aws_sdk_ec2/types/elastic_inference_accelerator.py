"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticInferenceAccelerator``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.elastic_inference_accelerator_count
    import aws_sdk_ec2.types.string


class ElasticInferenceAccelerator(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The type of elastic inference accelerator. The possible values are <code>eia1.medium</code>, <code>eia1.large</code>, <code>eia1.xlarge</code>, <code>eia2.medium</code>, <code>eia2.large</code>, and <code>eia2.xlarge</code>. </p>"""
    count: NotRequired[
        "aws_sdk_ec2.types.elastic_inference_accelerator_count.ElasticInferenceAcceleratorCount"
    ]
    """<p> The number of elastic inference accelerators to attach to the instance. </p> <p>Default: 1</p>"""
