"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceLoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_logs


class VerifiedAccessInstanceLoggingConfiguration(TypedDict):
    verified_access_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access instance.</p>"""
    access_logs: NotRequired[
        "aws_sdk_ec2.types.verified_access_logs.VerifiedAccessLogs"
    ]
    """<p>Details about the logging options.</p>"""
