"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#VpcTransitConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list
    import aws_sdk_gameliftstreams.types.vpc_id


class VpcTransitConfiguration(TypedDict, closed=True):
    vpc_id: "aws_sdk_gameliftstreams.types.vpc_id.VpcId"
    """<p>The ID of the Amazon VPC that you want to connect to the stream group. The VPC must be in the same Amazon Web Services account as the stream group. This value cannot be changed after the stream group is created.</p>"""
    ipv4_cidr_blocks: (
        "aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.Ipv4CidrBlockList"
    )
    """<p>A list of IPv4 CIDR blocks in your VPC that you want the stream group to be able to access. You can specify up to 5 CIDR blocks. The CIDR blocks must be valid subsets of the VPC's CIDR blocks and cannot overlap with the service VPC CIDR block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcTransitConfiguration) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list

    out["Ipv4CidrBlocks"] = (
        aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.serialize_json(
            value["ipv4_cidr_blocks"]
        )
    )
    return out


def deserialize_json(data: dict) -> VpcTransitConfiguration:
    out: VpcTransitConfiguration = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("VpcTransitConfiguration.vpc_id required")
    if "Ipv4CidrBlocks" in data:
        import aws_sdk_gameliftstreams.types.ipv4_cidr_block_list

        out["ipv4_cidr_blocks"] = (
            aws_sdk_gameliftstreams.types.ipv4_cidr_block_list.deserialize_json(
                data["Ipv4CidrBlocks"]
            )
        )
    else:
        raise DeserializationError("VpcTransitConfiguration.ipv4_cidr_blocks required")
    return out
