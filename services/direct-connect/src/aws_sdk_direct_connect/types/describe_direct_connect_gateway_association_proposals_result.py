"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAssociationProposalsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list
    import aws_sdk_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAssociationProposalsResult(TypedDict):
    direct_connect_gateway_association_proposals: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list.DirectConnectGatewayAssociationProposalList"
    ]
    """<p>Describes the Direct Connect gateway association proposals.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAssociationProposalsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association_proposals" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["directConnectGatewayAssociationProposals"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list.serialize_aws_json_1_1(
                value["direct_connect_gateway_association_proposals"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAssociationProposalsResult:
    out: DescribeDirectConnectGatewayAssociationProposalsResult = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayAssociationProposals" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list

        out["direct_connect_gateway_association_proposals"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association_proposal_list.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociationProposals"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
