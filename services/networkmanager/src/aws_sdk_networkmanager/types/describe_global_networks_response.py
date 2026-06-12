"""Generated from Smithy shape ``com.amazonaws.networkmanager#DescribeGlobalNetworksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_list
    import aws_sdk_networkmanager.types.next_token


class DescribeGlobalNetworksResponse(TypedDict):
    global_networks: NotRequired[
        "aws_sdk_networkmanager.types.global_network_list.GlobalNetworkList"
    ]
    """<p>Information about the global networks.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGlobalNetworksResponse) -> dict:
    out: dict = {}
    if "global_networks" in value:
        import aws_sdk_networkmanager.types.global_network_list

        out["GlobalNetworks"] = (
            aws_sdk_networkmanager.types.global_network_list.serialize_json(
                value["global_networks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeGlobalNetworksResponse:
    out: DescribeGlobalNetworksResponse = {}  # type: ignore[typeddict-item]
    if "GlobalNetworks" in data:
        import aws_sdk_networkmanager.types.global_network_list

        out["global_networks"] = (
            aws_sdk_networkmanager.types.global_network_list.deserialize_json(
                data["GlobalNetworks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
