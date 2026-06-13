"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#VpcTransitConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list
    import aws_sdk_gameliftstreams.types.vpc_id


class VpcTransitConfigurationResponse(TypedDict):
    vpc_id: NotRequired["aws_sdk_gameliftstreams.types.vpc_id.VpcId"]
    """<p>The ID of the Amazon VPC that is connected to the stream group.</p>"""
    ipv4_cidr_blocks: NotRequired[
        "aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.Ipv4CidrBlockList"
    ]
    """<p>The IPv4 CIDR blocks in your VPC that the stream group can access.</p>"""
    transit_gateway_id: NotRequired["str"]
    """<p>The ID of the Transit Gateway that Amazon GameLift Streams created for this VPC connection. Use this ID when creating your VPC attachment.</p>"""
    transit_gateway_resource_share_arn: NotRequired["str"]
    """<p>The ARN of the AWS Resource Access Manager resource share for the Transit Gateway. You must accept this resource share before you can create a VPC attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcTransitConfigurationResponse) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "ipv4_cidr_blocks" in value:
        import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list

        out["Ipv4CidrBlocks"] = (
            aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.serialize_json(
                value["ipv4_cidr_blocks"]
            )
        )
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
    if "transit_gateway_resource_share_arn" in value:
        out["TransitGatewayResourceShareArn"] = value[
            "transit_gateway_resource_share_arn"
        ]
    return out


def deserialize_json(data: dict) -> VpcTransitConfigurationResponse:
    out: VpcTransitConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Ipv4CidrBlocks" in data:
        import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list

        out["ipv4_cidr_blocks"] = (
            aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.deserialize_json(
                data["Ipv4CidrBlocks"]
            )
        )
    if "TransitGatewayId" in data:
        out["transit_gateway_id"] = data["TransitGatewayId"]
    if "TransitGatewayResourceShareArn" in data:
        out["transit_gateway_resource_share_arn"] = data[
            "TransitGatewayResourceShareArn"
        ]
    return out
