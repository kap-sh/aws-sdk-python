"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisComponent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AnalysisComponent(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the component.</p>"""
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the analysis component.</p>"""
