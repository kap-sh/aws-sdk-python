"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpQueryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.http_query_parameter

HttpQueryParameters: TypeAlias = list[
    "capo_app_mesh.types.http_query_parameter.HttpQueryParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpQueryParameters) -> list:
    import capo_app_mesh.types.http_query_parameter

    out: list = []
    for item in value:
        out.append(capo_app_mesh.types.http_query_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> HttpQueryParameters:
    import capo_app_mesh.types.http_query_parameter

    out: HttpQueryParameters = []
    for item in data:
        out.append(capo_app_mesh.types.http_query_parameter.deserialize_json(item))
    return out
