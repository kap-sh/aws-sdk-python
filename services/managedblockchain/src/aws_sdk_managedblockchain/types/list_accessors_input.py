"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListAccessorsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_list_max_results
    import aws_sdk_managedblockchain.types.accessor_network_type
    import aws_sdk_managedblockchain.types.pagination_token


class ListAccessorsInput(TypedDict):
    max_results: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_list_max_results.AccessorListMaxResults"
    ]
    """<p> The maximum number of accessors to list.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p> The pagination token that indicates the next set of results to retrieve. </p>"""
    network_type: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the <code>Accessor</code> token is created for.</p> <note> <p>Use the value <code>ETHEREUM_MAINNET_AND_GOERLI</code> for all existing <code>Accessors</code> tokens that were created before the <code>networkType</code> property was introduced.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessorsInput:
    out: ListAccessorsInput = {}  # type: ignore[typeddict-item]
    return out
