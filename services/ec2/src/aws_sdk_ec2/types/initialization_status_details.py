"""Generated from Smithy shape ``com.amazonaws.ec2#InitializationStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.initialization_type
    import aws_sdk_ec2.types.long


class InitializationStatusDetails(TypedDict):
    initialization_type: NotRequired[
        "aws_sdk_ec2.types.initialization_type.InitializationType"
    ]
    """<p>The method used for volume initialization. Possible values include:</p> <ul> <li> <p> <code>default</code> - Volume initialized using the default volume initialization rate or fast snapshot restore.</p> </li> <li> <p> <code>provisioned-rate</code> - Volume initialized using an Amazon EBS Provisioned Rate for Volume Initialization.</p> </li> <li> <p> <code>volume-copy</code> - Volume copy initialized at the rate for volume copies.</p> </li> </ul>"""
    progress: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The current volume initialization progress as a percentage (0-100). Returns <code>100</code> when volume initialization has completed.</p>"""
    estimated_time_to_complete_in_seconds: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The estimated remaining time, in seconds, for volume initialization to complete. Returns <code>0</code> when volume initialization has completed.</p> <p>Only available for volumes created with Amazon EBS Provisioned Rate for Volume Initialization.</p>"""
