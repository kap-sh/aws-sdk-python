"""Generated from Smithy shape ``com.amazonaws.s3outposts#CreateEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.customer_owned_ipv4_pool
    import aws_sdk_s3outposts.types.endpoint_access_type
    import aws_sdk_s3outposts.types.outpost_id
    import aws_sdk_s3outposts.types.security_group_id
    import aws_sdk_s3outposts.types.subnet_id


class CreateEndpointRequest(TypedDict, closed=True):
    outpost_id: "aws_sdk_s3outposts.types.outpost_id.OutpostId"
    """<p>The ID of the Outposts. </p>"""
    subnet_id: "aws_sdk_s3outposts.types.subnet_id.SubnetId"
    """<p>The ID of the subnet in the selected VPC. The endpoint subnet must belong to the Outpost that has Amazon S3 on Outposts provisioned.</p>"""
    security_group_id: "aws_sdk_s3outposts.types.security_group_id.SecurityGroupId"
    """<p>The ID of the security group to use with the endpoint.</p>"""
    access_type: NotRequired[
        "aws_sdk_s3outposts.types.endpoint_access_type.EndpointAccessType"
    ]
    """<p>The type of access for the network connectivity for the Amazon S3 on Outposts endpoint. To use the Amazon Web Services VPC, choose <code>Private</code>. To use the endpoint with an on-premises network, choose <code>CustomerOwnedIp</code>. If you choose <code>CustomerOwnedIp</code>, you must also provide the customer-owned IP address pool (CoIP pool).</p> <note> <p> <code>Private</code> is the default access type value.</p> </note>"""
    customer_owned_ipv4_pool: NotRequired[
        "aws_sdk_s3outposts.types.customer_owned_ipv4_pool.CustomerOwnedIpv4Pool"
    ]
    """<p>The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointRequest) -> dict:
    out: dict = {}
    out["OutpostId"] = value["outpost_id"]
    out["SubnetId"] = value["subnet_id"]
    out["SecurityGroupId"] = value["security_group_id"]
    if "access_type" in value:
        import aws_sdk_s3outposts.types.endpoint_access_type

        out["AccessType"] = (
            aws_sdk_s3outposts.types.endpoint_access_type.serialize_json(
                value["access_type"]
            )
        )
    if "customer_owned_ipv4_pool" in value:
        out["CustomerOwnedIpv4Pool"] = value["customer_owned_ipv4_pool"]
    return out


def deserialize_json(data: dict) -> CreateEndpointRequest:
    out: CreateEndpointRequest = {}  # type: ignore[typeddict-item]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    else:
        raise DeserializationError("CreateEndpointRequest.outpost_id required")
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    else:
        raise DeserializationError("CreateEndpointRequest.subnet_id required")
    if "SecurityGroupId" in data:
        out["security_group_id"] = data["SecurityGroupId"]
    else:
        raise DeserializationError("CreateEndpointRequest.security_group_id required")
    if "AccessType" in data:
        import aws_sdk_s3outposts.types.endpoint_access_type

        out["access_type"] = (
            aws_sdk_s3outposts.types.endpoint_access_type.deserialize_json(
                data["AccessType"]
            )
        )
    if "CustomerOwnedIpv4Pool" in data:
        out["customer_owned_ipv4_pool"] = data["CustomerOwnedIpv4Pool"]
    return out
