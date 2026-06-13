"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRouteHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_route_header

HttpRouteHeaders: TypeAlias = list[
    "aws_sdk_app_mesh.types.http_route_header.HttpRouteHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpRouteHeaders) -> list:
    import aws_sdk_app_mesh.types.http_route_header

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.http_route_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> HttpRouteHeaders:
    import aws_sdk_app_mesh.types.http_route_header

    out: HttpRouteHeaders = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.http_route_header.deserialize_json(item))
    return out
