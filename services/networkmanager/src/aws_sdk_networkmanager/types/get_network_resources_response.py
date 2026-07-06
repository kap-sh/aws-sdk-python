"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetNetworkResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.network_resource_list
    import aws_sdk_networkmanager.types.next_token


class GetNetworkResourcesResponse(TypedDict, closed=True):
    network_resources: NotRequired[
        "aws_sdk_networkmanager.types.network_resource_list.NetworkResourceList"
    ]
    """<p>The network resources.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkResourcesResponse) -> dict:
    out: dict = {}
    if "network_resources" in value:
        import aws_sdk_networkmanager.types.network_resource_list

        out["NetworkResources"] = (
            aws_sdk_networkmanager.types.network_resource_list.serialize_json(
                value["network_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetNetworkResourcesResponse:
    out: GetNetworkResourcesResponse = {}  # type: ignore[typeddict-item]
    if "NetworkResources" in data:
        import aws_sdk_networkmanager.types.network_resource_list

        out["network_resources"] = (
            aws_sdk_networkmanager.types.network_resource_list.deserialize_json(
                data["NetworkResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
