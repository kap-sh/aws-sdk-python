"""Generated from Smithy shape ``com.amazonaws.managedblockchain#ListNetworksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.network_summary_list
    import capo_managedblockchain.types.pagination_token


class ListNetworksOutput(TypedDict, closed=True):
    networks: NotRequired[
        "capo_managedblockchain.types.network_summary_list.NetworkSummaryList"
    ]
    """<p>An array of <code>NetworkSummary</code> objects that contain configuration properties for each network.</p>"""
    next_token: NotRequired[
        "capo_managedblockchain.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksOutput) -> dict:
    out: dict = {}
    if "networks" in value:
        import capo_managedblockchain.types.network_summary_list

        out["Networks"] = (
            capo_managedblockchain.types.network_summary_list.serialize_json(
                value["networks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworksOutput:
    out: ListNetworksOutput = {}  # type: ignore[typeddict-item]
    if "Networks" in data:
        import capo_managedblockchain.types.network_summary_list

        out["networks"] = (
            capo_managedblockchain.types.network_summary_list.deserialize_json(
                data["Networks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
