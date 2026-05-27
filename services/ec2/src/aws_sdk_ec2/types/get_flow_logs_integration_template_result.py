"""Generated from Smithy shape ``com.amazonaws.ec2#GetFlowLogsIntegrationTemplateResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class GetFlowLogsIntegrationTemplateResult(TypedDict):
    result: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The generated CloudFormation template.</p>"""
