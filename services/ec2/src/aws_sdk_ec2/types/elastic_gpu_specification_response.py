"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecificationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ElasticGpuSpecificationResponse(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Deprecated.</p> <note> <p>Amazon Elastic Graphics reached end of life on January 8, 2024.</p> </note>"""
