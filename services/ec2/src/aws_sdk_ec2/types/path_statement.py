"""Generated from Smithy shape ``com.amazonaws.ec2#PathStatement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.packet_header_statement
    import aws_sdk_ec2.types.resource_statement


class PathStatement(TypedDict):
    packet_header_statement: NotRequired[
        "aws_sdk_ec2.types.packet_header_statement.PacketHeaderStatement"
    ]
    """<p>The packet header statement.</p>"""
    resource_statement: NotRequired[
        "aws_sdk_ec2.types.resource_statement.ResourceStatement"
    ]
    """<p>The resource statement.</p>"""
