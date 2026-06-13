"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpQueryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.http_query_parameter

HttpQueryParameters: TypeAlias = list[
    "aws_sdk_app_mesh.types.http_query_parameter.HttpQueryParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpQueryParameters) -> list:
    import aws_sdk_app_mesh.types.http_query_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_app_mesh.types.http_query_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> HttpQueryParameters:
    import aws_sdk_app_mesh.types.http_query_parameter

    out: HttpQueryParameters = []
    for item in data:
        out.append(aws_sdk_app_mesh.types.http_query_parameter.deserialize_json(item))
    return out
