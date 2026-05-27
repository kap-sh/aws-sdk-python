"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceMetadataDefaultsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_metadata_defaults_response


class GetInstanceMetadataDefaultsResult(TypedDict):
    account_level: NotRequired[
        "aws_sdk_ec2.types.instance_metadata_defaults_response.InstanceMetadataDefaultsResponse"
    ]
    """<p>The account-level default IMDS settings.</p>"""
