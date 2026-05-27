"""Generated from Smithy shape ``com.amazonaws.ec2#ElasticGpuSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ElasticGpuSpecification(TypedDict):
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of Elastic Graphics accelerator.</p>"""
