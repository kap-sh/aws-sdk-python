"""Generated from Smithy shape ``com.amazonaws.ec2#IntegrateServices``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.athena_integrations_set


class IntegrateServices(TypedDict):
    athena_integrations: NotRequired[
        "aws_sdk_ec2.types.athena_integrations_set.AthenaIntegrationsSet"
    ]
    """<p>Information about the integration with Amazon Athena.</p>"""
