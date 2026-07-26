"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpcPeeringConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details
    import capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details
    import capo_securityhub.types.non_empty_string


class AwsEc2VpcPeeringConnectionDetails(TypedDict, closed=True):
    accepter_vpc_info: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.AwsEc2VpcPeeringConnectionVpcInfoDetails"
    ]
    """<p>Information about the accepter VPC. </p>"""
    expiration_time: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The time at which an unaccepted VPC peering connection will expire. </p>"""
    requester_vpc_info: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.AwsEc2VpcPeeringConnectionVpcInfoDetails"
    ]
    """<p>Information about the requester VPC. </p>"""
    status: NotRequired[
        "capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details.AwsEc2VpcPeeringConnectionStatusDetails"
    ]
    """<p>The status of the VPC peering connection. </p>"""
    vpc_peering_connection_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the VPC peering connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpcPeeringConnectionDetails) -> dict:
    out: dict = {}
    if "accepter_vpc_info" in value:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["AccepterVpcInfo"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.serialize_json(
                value["accepter_vpc_info"]
            )
        )
    if "expiration_time" in value:
        out["ExpirationTime"] = value["expiration_time"]
    if "requester_vpc_info" in value:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["RequesterVpcInfo"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.serialize_json(
                value["requester_vpc_info"]
            )
        )
    if "status" in value:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details

        out["Status"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details.serialize_json(
                value["status"]
            )
        )
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpcPeeringConnectionDetails:
    out: AwsEc2VpcPeeringConnectionDetails = {}  # type: ignore[typeddict-item]
    if "AccepterVpcInfo" in data:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["accepter_vpc_info"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.deserialize_json(
                data["AccepterVpcInfo"]
            )
        )
    if "ExpirationTime" in data:
        out["expiration_time"] = data["ExpirationTime"]
    if "RequesterVpcInfo" in data:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details

        out["requester_vpc_info"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_vpc_info_details.deserialize_json(
                data["RequesterVpcInfo"]
            )
        )
    if "Status" in data:
        import capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details

        out["status"] = (
            capo_securityhub.types.aws_ec2_vpc_peering_connection_status_details.deserialize_json(
                data["Status"]
            )
        )
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    return out
