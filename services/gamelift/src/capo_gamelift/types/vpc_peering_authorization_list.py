"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcPeeringAuthorizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_peering_authorization

VpcPeeringAuthorizationList: TypeAlias = list[
    "capo_gamelift.types.vpc_peering_authorization.VpcPeeringAuthorization"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcPeeringAuthorizationList) -> list:
    import capo_gamelift.types.vpc_peering_authorization

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.vpc_peering_authorization.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcPeeringAuthorizationList:
    import capo_gamelift.types.vpc_peering_authorization

    out: VpcPeeringAuthorizationList = []
    for item in data:
        out.append(
            capo_gamelift.types.vpc_peering_authorization.deserialize_aws_json_1_1(item)
        )
    return out
