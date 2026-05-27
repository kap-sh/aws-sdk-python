"""Generated from Smithy shape ``com.amazonaws.ec2#PacketHeaderStatement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_list
    import aws_sdk_ec2.types.value_string_list


class PacketHeaderStatement(TypedDict):
    source_addresses: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source addresses.</p>"""
    destination_addresses: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination addresses.</p>"""
    source_ports: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination ports.</p>"""
    source_prefix_lists: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The source prefix lists.</p>"""
    destination_prefix_lists: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination prefix lists.</p>"""
    protocols: NotRequired["aws_sdk_ec2.types.protocol_list.ProtocolList"]
    """<p>The protocols.</p>"""
