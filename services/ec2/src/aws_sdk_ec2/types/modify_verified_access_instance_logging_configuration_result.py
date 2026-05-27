"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessInstanceLoggingConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance_logging_configuration


class ModifyVerifiedAccessInstanceLoggingConfigurationResult(TypedDict):
    logging_configuration: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance_logging_configuration.VerifiedAccessInstanceLoggingConfiguration"
    ]
    """<p>The logging configuration for the Verified Access instance.</p>"""
