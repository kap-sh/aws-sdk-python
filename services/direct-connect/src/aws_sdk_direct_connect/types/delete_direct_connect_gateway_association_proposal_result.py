"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayAssociationProposalResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal


class DeleteDirectConnectGatewayAssociationProposalResult(TypedDict):
    direct_connect_gateway_association_proposal: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.DirectConnectGatewayAssociationProposal"
    ]
    """<p>The ID of the associated gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteDirectConnectGatewayAssociationProposalResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposal" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

        out["directConnectGatewayAssociationProposal"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.serialize_aws_json_1_1(
                value["direct_connect_gateway_association_proposal"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteDirectConnectGatewayAssociationProposalResult:
    out: DeleteDirectConnectGatewayAssociationProposalResult = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayAssociationProposal" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

        out["direct_connect_gateway_association_proposal"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociationProposal"]
            )
        )
    return out
