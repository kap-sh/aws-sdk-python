"""Generated from Smithy shape ``com.amazonaws.securityagent#ListDiscoveredEndpointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.discovered_endpoint_list
    import aws_sdk_securityagent.types.next_token


class ListDiscoveredEndpointsOutput(TypedDict):
    discovered_endpoints: NotRequired[
        "aws_sdk_securityagent.types.discovered_endpoint_list.DiscoveredEndpointList"
    ]
    """<p>The list of discovered endpoints.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoveredEndpointsOutput) -> dict:
    out: dict = {}
    if "discovered_endpoints" in value:
        import aws_sdk_securityagent.types.discovered_endpoint_list

        out["discoveredEndpoints"] = (
            aws_sdk_securityagent.types.discovered_endpoint_list.serialize_json(
                value["discovered_endpoints"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoveredEndpointsOutput:
    out: ListDiscoveredEndpointsOutput = {}  # type: ignore[typeddict-item]
    if "discoveredEndpoints" in data:
        import aws_sdk_securityagent.types.discovered_endpoint_list

        out["discovered_endpoints"] = (
            aws_sdk_securityagent.types.discovered_endpoint_list.deserialize_json(
                data["discoveredEndpoints"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
