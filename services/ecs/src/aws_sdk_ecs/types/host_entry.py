"""Generated from Smithy shape ``com.amazonaws.ecs#HostEntry``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class HostEntry(TypedDict):
    hostname: "aws_sdk_ecs.types.string.String"
    """<p>The hostname to use in the <code>/etc/hosts</code> entry.</p>"""
    ip_address: "aws_sdk_ecs.types.string.String"
    """<p>The IP address to use in the <code>/etc/hosts</code> entry.</p>"""
