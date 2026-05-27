"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointRdsOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_port_number


class ModifyVerifiedAccessEndpointRdsOptions(TypedDict):
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list.ModifyVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The port.</p>"""
    rds_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The RDS endpoint.</p>"""
