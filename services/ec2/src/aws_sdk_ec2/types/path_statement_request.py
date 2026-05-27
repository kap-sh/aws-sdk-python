"""Generated from Smithy shape ``com.amazonaws.ec2#PathStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.packet_header_statement_request
    import aws_sdk_ec2.types.resource_statement_request


class PathStatementRequest(TypedDict):
    packet_header_statement: NotRequired[
        "aws_sdk_ec2.types.packet_header_statement_request.PacketHeaderStatementRequest"
    ]
    """<p>The packet header statement.</p>"""
    resource_statement: NotRequired[
        "aws_sdk_ec2.types.resource_statement_request.ResourceStatementRequest"
    ]
    """<p>The resource statement.</p>"""
