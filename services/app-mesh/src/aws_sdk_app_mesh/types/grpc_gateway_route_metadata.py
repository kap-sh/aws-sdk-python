"""Generated from Smithy shape ``com.amazonaws.appmesh#GrpcGatewayRouteMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.grpc_metadata_match_method
    import aws_sdk_app_mesh.types.header_name


class GrpcGatewayRouteMetadata(TypedDict):
    name: "aws_sdk_app_mesh.types.header_name.HeaderName"
    """<p>A name for the gateway route metadata.</p>"""
    invert: NotRequired["bool"]
    """<p>Specify <code>True</code> to match anything except the match criteria. The default value is <code>False</code>.</p>"""
    match: NotRequired[
        "aws_sdk_app_mesh.types.grpc_metadata_match_method.GrpcMetadataMatchMethod"
    ]
    """<p>The criteria for determining a metadata match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrpcGatewayRouteMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "invert" in value:
        out["invert"] = value["invert"]
    if "match" in value:
        import aws_sdk_app_mesh.types.grpc_metadata_match_method

        out["match"] = aws_sdk_app_mesh.types.grpc_metadata_match_method.serialize_json(
            value["match"]
        )
    return out


def deserialize_json(data: dict) -> GrpcGatewayRouteMetadata:
    out: GrpcGatewayRouteMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GrpcGatewayRouteMetadata.name required")
    if "invert" in data:
        out["invert"] = data["invert"]
    if "match" in data:
        import aws_sdk_app_mesh.types.grpc_metadata_match_method

        out["match"] = (
            aws_sdk_app_mesh.types.grpc_metadata_match_method.deserialize_json(
                data["match"]
            )
        )
    return out
