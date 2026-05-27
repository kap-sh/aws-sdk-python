"""Generated from Smithy shape ``com.amazonaws.ec2#PtrUpdateStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PtrUpdateStatus(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value for the PTR record update.</p>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status of the PTR record update.</p>"""
    reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the PTR record update.</p>"""
