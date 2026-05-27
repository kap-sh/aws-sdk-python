"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_statement_request


class ThroughResourcesStatementRequest(TypedDict):
    resource_statement: NotRequired[
        "aws_sdk_ec2.types.resource_statement_request.ResourceStatementRequest"
    ]
    """<p>The resource statement.</p>"""
