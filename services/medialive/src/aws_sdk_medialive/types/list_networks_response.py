"""Generated from Smithy shape ``com.amazonaws.medialive#ListNetworksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_describe_network_summary
    import aws_sdk_medialive.types.__string


class ListNetworksResponse(TypedDict):
    networks: NotRequired[
        "aws_sdk_medialive.types.__list_of_describe_network_summary.__listOfDescribeNetworkSummary"
    ]
    """An array of networks that you have created."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token for the next ListNetworks request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworksResponse) -> dict:
    out: dict = {}
    if "networks" in value:
        import aws_sdk_medialive.types.__list_of_describe_network_summary

        out["networks"] = (
            aws_sdk_medialive.types.__list_of_describe_network_summary.serialize_json(
                value["networks"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworksResponse:
    out: ListNetworksResponse = {}  # type: ignore[typeddict-item]
    if "networks" in data:
        import aws_sdk_medialive.types.__list_of_describe_network_summary

        out["networks"] = (
            aws_sdk_medialive.types.__list_of_describe_network_summary.deserialize_json(
                data["networks"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
