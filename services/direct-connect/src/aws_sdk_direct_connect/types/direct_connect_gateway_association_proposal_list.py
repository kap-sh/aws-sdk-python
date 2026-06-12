"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociationProposalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

DirectConnectGatewayAssociationProposalList: TypeAlias = list[
    "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.DirectConnectGatewayAssociationProposal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociationProposalList) -> list:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectConnectGatewayAssociationProposalList:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

    out: DirectConnectGatewayAssociationProposalList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.deserialize_aws_json_1_1(
                item
            )
        )
    return out
