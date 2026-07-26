"""Generated from Smithy shape ``com.amazonaws.medialive#ListNetworksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_describe_network_summary
    import capo_medialive.types.__string


class ListNetworksResponse(TypedDict, closed=True):
    networks: NotRequired[
        "capo_medialive.types.__list_of_describe_network_summary.__listOfDescribeNetworkSummary"
    ]
    """An array of networks that you have created."""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """Token for the next ListNetworks request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksResponse) -> dict:
    out: dict = {}
    if "networks" in value:
        import capo_medialive.types.__list_of_describe_network_summary

        out["networks"] = (
            capo_medialive.types.__list_of_describe_network_summary.serialize_json(
                value["networks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworksResponse:
    out: ListNetworksResponse = {}  # type: ignore[typeddict-item]
    if "networks" in data:
        import capo_medialive.types.__list_of_describe_network_summary

        out["networks"] = (
            capo_medialive.types.__list_of_describe_network_summary.deserialize_json(
                data["networks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
