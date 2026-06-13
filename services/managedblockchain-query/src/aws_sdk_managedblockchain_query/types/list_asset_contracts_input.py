"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ListAssetContractsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.contract_filter
    import aws_sdk_managedblockchain_query.types.next_token


class ListAssetContractsInput(TypedDict):
    contract_filter: (
        "aws_sdk_managedblockchain_query.types.contract_filter.ContractFilter"
    )
    """<p>Contains the filter parameter for the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain_query.types.next_token.NextToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of contracts to list.</p> <p>Default: <code>100</code> </p> <note> <p>Even if additional results can be retrieved, the request can return less results than <code>maxResults</code> or an empty array of results.</p> <p>To retrieve the next set of results, make another request with the returned <code>nextToken</code> value. The value of <code>nextToken</code> is <code>null</code> when there are no more results to return</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetContractsInput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.contract_filter

    out["contractFilter"] = (
        aws_sdk_managedblockchain_query.types.contract_filter.serialize_json(
            value["contract_filter"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAssetContractsInput:
    out: ListAssetContractsInput = {}  # type: ignore[typeddict-item]
    if "contractFilter" in data:
        import aws_sdk_managedblockchain_query.types.contract_filter

        out["contract_filter"] = (
            aws_sdk_managedblockchain_query.types.contract_filter.deserialize_json(
                data["contractFilter"]
            )
        )
    else:
        raise DeserializationError("ListAssetContractsInput.contract_filter required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
