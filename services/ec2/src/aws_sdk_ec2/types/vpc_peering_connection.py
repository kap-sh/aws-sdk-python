"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_peering_connection_state_reason
    import aws_sdk_ec2.types.vpc_peering_connection_vpc_info


class VpcPeeringConnection(TypedDict):
    accepter_vpc_info: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the accepter VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    expiration_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that an unaccepted VPC peering connection will expire.</p>"""
    requester_vpc_info: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_vpc_info.VpcPeeringConnectionVpcInfo"
    ]
    """<p>Information about the requester VPC. CIDR block information is only returned when describing an active VPC peering connection.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_state_reason.VpcPeeringConnectionStateReason"
    ]
    """<p>The status of the VPC peering connection.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC peering connection.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcPeeringConnection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "accepter_vpc_info" in value:
        import aws_sdk_ec2.types.vpc_peering_connection_vpc_info

        aws_sdk_ec2.types.vpc_peering_connection_vpc_info.serialize_ec2_query(
            value["accepter_vpc_info"], pairs, f"{prefix}.AccepterVpcInfo"
        )
    if "expiration_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["expiration_time"], pairs, f"{prefix}.ExpirationTime"
        )
    if "requester_vpc_info" in value:
        import aws_sdk_ec2.types.vpc_peering_connection_vpc_info

        aws_sdk_ec2.types.vpc_peering_connection_vpc_info.serialize_ec2_query(
            value["requester_vpc_info"], pairs, f"{prefix}.RequesterVpcInfo"
        )
    if "status" in value:
        import aws_sdk_ec2.types.vpc_peering_connection_state_reason

        aws_sdk_ec2.types.vpc_peering_connection_state_reason.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> VpcPeeringConnection:
    out: VpcPeeringConnection = {}  # type: ignore[typeddict-item]
    child_accepter_vpc_info = el.find("AccepterVpcInfo")
    if child_accepter_vpc_info is not None:
        import aws_sdk_ec2.types.vpc_peering_connection_vpc_info

        out["accepter_vpc_info"] = (
            aws_sdk_ec2.types.vpc_peering_connection_vpc_info.deserialize_ec2_query(
                child_accepter_vpc_info
            )
        )
    child_expiration_time = el.find("ExpirationTime")
    if child_expiration_time is not None:
        import aws_sdk_ec2.types.date_time

        out["expiration_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_expiration_time
        )
    child_requester_vpc_info = el.find("RequesterVpcInfo")
    if child_requester_vpc_info is not None:
        import aws_sdk_ec2.types.vpc_peering_connection_vpc_info

        out["requester_vpc_info"] = (
            aws_sdk_ec2.types.vpc_peering_connection_vpc_info.deserialize_ec2_query(
                child_requester_vpc_info
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.vpc_peering_connection_state_reason

        out["status"] = (
            aws_sdk_ec2.types.vpc_peering_connection_state_reason.deserialize_ec2_query(
                child_status
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    return out
