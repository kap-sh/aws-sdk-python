"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListProxyConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.proxy_configurations


class ListProxyConfigurationsResponse(TypedDict):
    proxy_configurations: NotRequired[
        "aws_sdk_network_firewall.types.proxy_configurations.ProxyConfigurations"
    ]
    """<p>The metadata for the proxy configurations. Depending on your setting for max results and the number of proxy configurations that you have, this might not be the full list. </p>"""
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProxyConfigurationsResponse) -> dict:
    out: dict = {}
    if "proxy_configurations" in value:
        import aws_sdk_network_firewall.types.proxy_configurations

        out["ProxyConfigurations"] = (
            aws_sdk_network_firewall.types.proxy_configurations.serialize_aws_json_1_0(
                value["proxy_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProxyConfigurationsResponse:
    out: ListProxyConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "ProxyConfigurations" in data:
        import aws_sdk_network_firewall.types.proxy_configurations

        out["proxy_configurations"] = (
            aws_sdk_network_firewall.types.proxy_configurations.deserialize_aws_json_1_0(
                data["ProxyConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
