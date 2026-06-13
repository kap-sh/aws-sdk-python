"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListTokenBalancesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.next_token
    import aws_sdk_managedblockchain_query.types.owner_filter
    import aws_sdk_managedblockchain_query.types.token_filter


class ListTokenBalancesInput(TypedDict):
    owner_filter: NotRequired[
        "aws_sdk_managedblockchain_query.types.owner_filter.OwnerFilter"
    ]
    """<p>The contract or wallet address on the blockchain network by which to filter the request. You must specify the <code>address</code> property of the <code>ownerFilter</code> when listing balances of tokens owned by the address.</p>"""
    token_filter: "aws_sdk_managedblockchain_query.types.token_filter.TokenFilter"
    """<p>The contract address or a token identifier on the blockchain network by which to filter the request. You must specify the <code>contractAddress</code> property of this container when listing tokens minted by a contract.</p> <note> <p>You must always specify the network property of this container when using this operation.</p> </note>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain_query.types.next_token.NextToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of token balances to return.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTokenBalancesInput) -> dict:
    out: dict = {}
    if "owner_filter" in value:
        import aws_sdk_managedblockchain_query.types.owner_filter

        out["ownerFilter"] = (
            aws_sdk_managedblockchain_query.types.owner_filter.serialize_json(
                value["owner_filter"]
            )
        )
    import aws_sdk_managedblockchain_query.types.token_filter

    out["tokenFilter"] = (
        aws_sdk_managedblockchain_query.types.token_filter.serialize_json(
            value["token_filter"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListTokenBalancesInput:
    out: ListTokenBalancesInput = {}  # type: ignore[typeddict-item]
    if "ownerFilter" in data:
        import aws_sdk_managedblockchain_query.types.owner_filter

        out["owner_filter"] = (
            aws_sdk_managedblockchain_query.types.owner_filter.deserialize_json(
                data["ownerFilter"]
            )
        )
    if "tokenFilter" in data:
        import aws_sdk_managedblockchain_query.types.token_filter

        out["token_filter"] = (
            aws_sdk_managedblockchain_query.types.token_filter.deserialize_json(
                data["tokenFilter"]
            )
        )
    else:
        raise DeserializationError("ListTokenBalancesInput.token_filter required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
