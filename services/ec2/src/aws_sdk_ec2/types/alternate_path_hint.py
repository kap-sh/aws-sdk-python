"""Generated from Smithy shape ``com.amazonaws.ec2#AlternatePathHint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AlternatePathHint(TypedDict):
    component_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the component.</p>"""
    component_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
