"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListNetworksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.framework
    import aws_sdk_managedblockchain.types.network_list_max_results
    import aws_sdk_managedblockchain.types.network_status
    import aws_sdk_managedblockchain.types.pagination_token
    import aws_sdk_managedblockchain.types.string


class ListNetworksInput(TypedDict):
    name: NotRequired["aws_sdk_managedblockchain.types.string.String"]
    """<p>The name of the network.</p>"""
    framework: NotRequired["aws_sdk_managedblockchain.types.framework.Framework"]
    """<p>An optional framework specifier. If provided, only networks of this framework type are listed.</p>"""
    status: NotRequired["aws_sdk_managedblockchain.types.network_status.NetworkStatus"]
    """<p>An optional status specifier. If provided, only networks currently in this status are listed.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    max_results: NotRequired[
        "aws_sdk_managedblockchain.types.network_list_max_results.NetworkListMaxResults"
    ]
    """<p>The maximum number of networks to list.</p>"""
    next_token: NotRequired[
        "aws_sdk_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNetworksInput:
    out: ListNetworksInput = {}  # type: ignore[typeddict-item]
    return out
