"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRouteHeader``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.header_match_method
    import aws_sdk_app_mesh.types.header_name


class HttpRouteHeader(TypedDict):
    name: "aws_sdk_app_mesh.types.header_name.HeaderName"
    """<p>A name for the HTTP header in the client request that will be matched on.</p>"""
    invert: NotRequired["bool"]
    """<p>Specify <code>True</code> to match anything except the match criteria. The default value is <code>False</code>.</p>"""
    match: NotRequired["aws_sdk_app_mesh.types.header_match_method.HeaderMatchMethod"]
    """<p>The <code>HeaderMatchMethod</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpRouteHeader) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "invert" in value:
        out["invert"] = value["invert"]
    if "match" in value:
        import aws_sdk_app_mesh.types.header_match_method

        out["match"] = aws_sdk_app_mesh.types.header_match_method.serialize_json(
            value["match"]
        )
    return out


def deserialize_json(data: dict) -> HttpRouteHeader:
    out: HttpRouteHeader = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HttpRouteHeader.name required")
    if "invert" in data:
        out["invert"] = data["invert"]
    if "match" in data:
        import aws_sdk_app_mesh.types.header_match_method

        out["match"] = aws_sdk_app_mesh.types.header_match_method.deserialize_json(
            data["match"]
        )
    return out
