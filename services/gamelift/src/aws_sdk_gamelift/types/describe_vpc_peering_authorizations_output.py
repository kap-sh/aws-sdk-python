"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeVpcPeeringAuthorizationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.vpc_peering_authorization_list


class DescribeVpcPeeringAuthorizationsOutput(TypedDict):
    vpc_peering_authorizations: NotRequired[
        "aws_sdk_gamelift.types.vpc_peering_authorization_list.VpcPeeringAuthorizationList"
    ]
    """<p>A collection of objects that describe all valid VPC peering operations for the current Amazon Web Services account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVpcPeeringAuthorizationsOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorizations" in value:
        import aws_sdk_gamelift.types.vpc_peering_authorization_list

        out["VpcPeeringAuthorizations"] = (
            aws_sdk_gamelift.types.vpc_peering_authorization_list.serialize_aws_json_1_1(
                value["vpc_peering_authorizations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVpcPeeringAuthorizationsOutput:
    out: DescribeVpcPeeringAuthorizationsOutput = {}  # type: ignore[typeddict-item]
    if "VpcPeeringAuthorizations" in data:
        import aws_sdk_gamelift.types.vpc_peering_authorization_list

        out["vpc_peering_authorizations"] = (
            aws_sdk_gamelift.types.vpc_peering_authorization_list.deserialize_aws_json_1_1(
                data["VpcPeeringAuthorizations"]
            )
        )
    return out
