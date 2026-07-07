"""Generated from Smithy shape ``com.amazonaws.directconnect#DeleteDirectConnectGatewayAssociationProposalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id


class DeleteDirectConnectGatewayAssociationProposalRequest(TypedDict, closed=True):
    proposal_id: "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
    """<p>The ID of the proposal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteDirectConnectGatewayAssociationProposalRequest,
) -> dict:
    out: dict = {}
    out["proposalId"] = value["proposal_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteDirectConnectGatewayAssociationProposalRequest:
    out: DeleteDirectConnectGatewayAssociationProposalRequest = {}  # type: ignore[typeddict-item]
    if "proposalId" in data:
        out["proposal_id"] = data["proposalId"]
    else:
        raise DeserializationError(
            "DeleteDirectConnectGatewayAssociationProposalRequest.proposal_id required"
        )
    return out
