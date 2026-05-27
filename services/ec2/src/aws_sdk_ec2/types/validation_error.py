"""Generated from Smithy shape ``com.amazonaws.ec2#ValidationError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ValidationError(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error code that indicates why the parameter or parameter combination is not valid. For more information about error codes, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html\">Error codes</a>.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message that describes why the parameter or parameter combination is not valid. For more information about error messages, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html\">Error codes</a>.</p>"""
