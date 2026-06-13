"""Generated from Smithy shape ``com.amazonaws.appmesh#GatewayRouteHostnameMatch``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.exact_host_name
    import aws_sdk_app_mesh.types.suffix_hostname


class GatewayRouteHostnameMatch(TypedDict):
    exact: NotRequired["aws_sdk_app_mesh.types.exact_host_name.ExactHostName"]
    """<p>The exact host name to match on.</p>"""
    suffix: NotRequired["aws_sdk_app_mesh.types.suffix_hostname.SuffixHostname"]
    """<p>The specified ending characters of the host name to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRouteHostnameMatch) -> dict:
    out: dict = {}
    if "exact" in value:
        out["exact"] = value["exact"]
    if "suffix" in value:
        out["suffix"] = value["suffix"]
    return out


def deserialize_json(data: dict) -> GatewayRouteHostnameMatch:
    out: GatewayRouteHostnameMatch = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        out["exact"] = data["exact"]
    if "suffix" in data:
        out["suffix"] = data["suffix"]
    return out
