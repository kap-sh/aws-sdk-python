"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcPeeringConnectionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details
    import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2VpcPeeringConnectionDetails(TypedDict):
    accepter_vpc_info: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.AwsEc2VpcPeeringConnectionVpcInfoDetails"
    ]
    """<p>Information about the accepter VPC. </p>"""
    expiration_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time at which an unaccepted VPC peering connection will expire. </p>"""
    requester_vpc_info: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.AwsEc2VpcPeeringConnectionVpcInfoDetails"
    ]
    """<p>Information about the requester VPC. </p>"""
    status: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details.AwsEc2VpcPeeringConnectionStatusDetails"
    ]
    """<p>The status of the VPC peering connection. </p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the VPC peering connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcPeeringConnectionDetails) -> dict:
    out: dict = {}
    if "accepter_vpc_info" in value:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["AccepterVpcInfo"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.serialize_json(
                value["accepter_vpc_info"]
            )
        )
    if "expiration_time" in value:
        out["ExpirationTime"] = value["expiration_time"]
    if "requester_vpc_info" in value:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["RequesterVpcInfo"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.serialize_json(
                value["requester_vpc_info"]
            )
        )
    if "status" in value:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details

        out["Status"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details.serialize_json(
                value["status"]
            )
        )
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcPeeringConnectionDetails:
    out: AwsEc2VpcPeeringConnectionDetails = {}  # type: ignore[typeddict-item]
    if "AccepterVpcInfo" in data:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["accepter_vpc_info"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.deserialize_json(
                data["AccepterVpcInfo"]
            )
        )
    if "ExpirationTime" in data:
        out["expiration_time"] = data["ExpirationTime"]
    if "RequesterVpcInfo" in data:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["requester_vpc_info"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.deserialize_json(
                data["RequesterVpcInfo"]
            )
        )
    if "Status" in data:
        import aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details

        out["status"] = (
            aws_sdk_securityhub.types.aws_ec2_vpc_peering_connection_status_details.deserialize_json(
                data["Status"]
            )
        )
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    return out
