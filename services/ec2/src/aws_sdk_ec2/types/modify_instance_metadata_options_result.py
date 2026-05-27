"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMetadataOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_metadata_options_response
    import aws_sdk_ec2.types.string


class ModifyInstanceMetadataOptionsResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_metadata_options: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_options_response.InstanceMetadataOptionsResponse"
    ]
    """<p>The metadata options for the instance.</p>"""
