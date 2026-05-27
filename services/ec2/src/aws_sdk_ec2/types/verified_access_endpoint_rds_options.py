"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointRdsOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_protocol
    import aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list


class VerifiedAccessEndpointRdsOptions(TypedDict):
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The port.</p>"""
    rds_db_instance_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the RDS instance.</p>"""
    rds_db_cluster_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the DB cluster.</p>"""
    rds_db_proxy_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the RDS proxy.</p>"""
    rds_endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The RDS endpoint.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list.VerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
