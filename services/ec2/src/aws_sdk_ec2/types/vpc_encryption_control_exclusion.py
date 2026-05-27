"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion_state


class VpcEncryptionControlExclusion(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusion_state.VpcEncryptionControlExclusionState"
    ]
    """<p>The current state of the exclusion configuration.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message providing additional information about the exclusion state.</p>"""
