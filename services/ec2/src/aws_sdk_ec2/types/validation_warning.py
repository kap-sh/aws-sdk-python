"""Generated from Smithy shape ``com.amazonaws.ec2#ValidationWarning``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.error_set


class ValidationWarning(TypedDict):
    errors: NotRequired["aws_sdk_ec2.types.error_set.ErrorSet"]
    """<p>The error codes and error messages.</p>"""
