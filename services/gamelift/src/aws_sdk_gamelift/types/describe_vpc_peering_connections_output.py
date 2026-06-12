"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeVpcPeeringConnectionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.vpc_peering_connection_list


class DescribeVpcPeeringConnectionsOutput(TypedDict):
    vpc_peering_connections: NotRequired[
        "aws_sdk_gamelift.types.vpc_peering_connection_list.VpcPeeringConnectionList"
    ]
    """<p>A collection of VPC peering connection records that match the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVpcPeeringConnectionsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_connections" in value:
        import aws_sdk_gamelift.types.vpc_peering_connection_list

        out["VpcPeeringConnections"] = (
            aws_sdk_gamelift.types.vpc_peering_connection_list.serialize_aws_json_1_1(
                value["vpc_peering_connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVpcPeeringConnectionsOutput:
    out: DescribeVpcPeeringConnectionsOutput = {}  # type: ignore[typeddict-item]
    if "VpcPeeringConnections" in data:
        import aws_sdk_gamelift.types.vpc_peering_connection_list

        out["vpc_peering_connections"] = (
            aws_sdk_gamelift.types.vpc_peering_connection_list.deserialize_aws_json_1_1(
                data["VpcPeeringConnections"]
            )
        )
    return out
