"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateElasticInferenceAcceleratorResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class LaunchTemplateElasticInferenceAcceleratorResponse(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of elastic inference accelerator. The possible values are eia1.medium, eia1.large, and eia1.xlarge. </p>"""
    count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of elastic inference accelerators to attach to the instance. </p>"""
