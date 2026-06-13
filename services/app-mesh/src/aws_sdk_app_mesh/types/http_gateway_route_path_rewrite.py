"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpGatewayRoutePathRewrite``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_path_exact


class HttpGatewayRoutePathRewrite(TypedDict):
    exact: NotRequired["aws_sdk_app_mesh.types.http_path_exact.HttpPathExact"]
    """<p>The exact path to rewrite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpGatewayRoutePathRewrite) -> dict:
    out: dict = {}
    if "exact" in value:
        out["exact"] = value["exact"]
    return out


def deserialize_json(data: dict) -> HttpGatewayRoutePathRewrite:
    out: HttpGatewayRoutePathRewrite = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        out["exact"] = data["exact"]
    return out
