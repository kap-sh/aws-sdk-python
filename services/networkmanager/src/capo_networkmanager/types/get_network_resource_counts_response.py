"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkResourceCountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.network_resource_count_list
    import capo_networkmanager.types.next_token


class GetNetworkResourceCountsResponse(TypedDict, closed=True):
    network_resource_counts: NotRequired[
        "capo_networkmanager.types.network_resource_count_list.NetworkResourceCountList"
    ]
    """<p>The count of resources.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResourceCountsResponse) -> dict:
    out: dict = {}
    if "network_resource_counts" in value:
        import capo_networkmanager.types.network_resource_count_list

        out["NetworkResourceCounts"] = (
            capo_networkmanager.types.network_resource_count_list.serialize_json(
                value["network_resource_counts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkResourceCountsResponse:
    out: GetNetworkResourceCountsResponse = {}  # type: ignore[typeddict-item]
    if "NetworkResourceCounts" in data:
        import capo_networkmanager.types.network_resource_count_list

        out["network_resource_counts"] = (
            capo_networkmanager.types.network_resource_count_list.deserialize_json(
                data["NetworkResourceCounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
