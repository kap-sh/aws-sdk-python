"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAssociationProposalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.associated_gateway_id
    import capo_direct_connect.types.direct_connect_gateway_association_proposal_id
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.max_result_set_size
    import capo_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAssociationProposalsRequest(TypedDict, closed=True):
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    proposal_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_proposal_id.DirectConnectGatewayAssociationProposalId"
    ]
    """<p>The ID of the proposal.</p>"""
    associated_gateway_id: NotRequired[
        "capo_direct_connect.types.associated_gateway_id.AssociatedGatewayId"
    ]
    """<p>The ID of the associated gateway.</p>"""
    max_results: NotRequired[
        "capo_direct_connect.types.max_result_set_size.MaxResultSetSize"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p> <p>If <code>MaxResults</code> is given a value larger than 100, only 100 results are returned.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAssociationProposalsRequest,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "proposal_id" in value:
        out["proposalId"] = value["proposal_id"]
    if "associated_gateway_id" in value:
        out["associatedGatewayId"] = value["associated_gateway_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationProposalsRequest:
    out: DescribeDirectConnectGatewayAssociationProposalsRequest = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "proposalId" in data:
        out["proposal_id"] = data["proposalId"]
    if "associatedGatewayId" in data:
        out["associated_gateway_id"] = data["associatedGatewayId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
