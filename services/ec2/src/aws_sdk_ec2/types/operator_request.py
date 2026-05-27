"""Generated from Smithy shape ``com.amazonaws.ec2#OperatorRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class OperatorRequest(TypedDict):
    principal: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The service provider that manages the resource.</p>"""
