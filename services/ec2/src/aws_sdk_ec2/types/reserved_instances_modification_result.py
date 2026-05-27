"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_configuration
    import aws_sdk_ec2.types.string


class ReservedInstancesModificationResult(TypedDict):
    reserved_instances_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID for the Reserved Instances that were created as part of the modification request. This field is only available when the modification is fulfilled.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_configuration.ReservedInstancesConfiguration"
    ]
    """<p>The target Reserved Instances configurations supplied as part of the modification request.</p>"""
