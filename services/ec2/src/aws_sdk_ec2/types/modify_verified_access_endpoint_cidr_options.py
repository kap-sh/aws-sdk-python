"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list


class ModifyVerifiedAccessEndpointCidrOptions(TypedDict):
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list.ModifyVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
