"""Generated from Smithy shape ``com.amazonaws.ec2#FpgaImageState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fpga_image_state_code
    import aws_sdk_ec2.types.string


class FpgaImageState(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.fpga_image_state_code.FpgaImageStateCode"]
    """<p>The state. The following are the possible values:</p> <ul> <li> <p> <code>pending</code> - AFI bitstream generation is in progress.</p> </li> <li> <p> <code>available</code> - The AFI is available for use.</p> </li> <li> <p> <code>failed</code> - AFI bitstream generation failed.</p> </li> <li> <p> <code>unavailable</code> - The AFI is no longer available for use.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the state is <code>failed</code>, this is the error message.</p>"""
