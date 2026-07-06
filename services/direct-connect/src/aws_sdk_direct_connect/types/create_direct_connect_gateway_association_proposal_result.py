"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayAssociationProposalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal


class CreateDirectConnectGatewayAssociationProposalResult(TypedDict, closed=True):
    direct_connect_gateway_association_proposal: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.DirectConnectGatewayAssociationProposal"
    ]
    """<p>Information about the Direct Connect gateway proposal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateDirectConnectGatewayAssociationProposalResult,
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
) -> CreateDirectConnectGatewayAssociationProposalResult:
    out: CreateDirectConnectGatewayAssociationProposalResult = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayAssociationProposal" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal

        out["direct_connect_gateway_association_proposal"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociationProposal"]
            )
        )
    return out
