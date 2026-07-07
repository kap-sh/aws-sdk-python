"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateVpcPeeringAuthorizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.vpc_peering_authorization


class CreateVpcPeeringAuthorizationOutput(TypedDict, closed=True):
    vpc_peering_authorization: NotRequired[
        "aws_sdk_gamelift.types.vpc_peering_authorization.VpcPeeringAuthorization"
    ]
    """<p>Details on the requested VPC peering authorization, including expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateVpcPeeringAuthorizationOutput) -> dict:
    out: dict = {}
    if "vpc_peering_authorization" in value:
        import aws_sdk_gamelift.types.vpc_peering_authorization

        out["VpcPeeringAuthorization"] = (
            aws_sdk_gamelift.types.vpc_peering_authorization.serialize_aws_json_1_1(
                value["vpc_peering_authorization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateVpcPeeringAuthorizationOutput:
    out: CreateVpcPeeringAuthorizationOutput = {}  # type: ignore[typeddict-item]
    if "VpcPeeringAuthorization" in data:
        import aws_sdk_gamelift.types.vpc_peering_authorization

        out["vpc_peering_authorization"] = (
            aws_sdk_gamelift.types.vpc_peering_authorization.deserialize_aws_json_1_1(
                data["VpcPeeringAuthorization"]
            )
        )
    return out
