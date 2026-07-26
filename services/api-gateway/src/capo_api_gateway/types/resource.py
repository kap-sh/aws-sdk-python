"""Generated from Smithy shape ``com.amazonaws.apigateway#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_method
    import capo_api_gateway.types.string


class Resource(TypedDict, closed=True):
    id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The resource's identifier.</p>"""
    parent_id: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The parent resource's identifier.</p>"""
    path_part: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The last path segment for this resource.</p>"""
    path: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The full path for this resource.</p>"""
    resource_methods: NotRequired["capo_api_gateway.types.map_of_method.MapOfMethod"]
    """<p>Gets an API resource's method of a given HTTP verb.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "parent_id" in value:
        out["parentId"] = value["parent_id"]
    if "path_part" in value:
        out["pathPart"] = value["path_part"]
    if "path" in value:
        out["path"] = value["path"]
    if "resource_methods" in value:
        import capo_api_gateway.types.map_of_method

        out["resourceMethods"] = capo_api_gateway.types.map_of_method.serialize_json(
            value["resource_methods"]
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "parentId" in data:
        out["parent_id"] = data["parentId"]
    if "pathPart" in data:
        out["path_part"] = data["pathPart"]
    if "path" in data:
        out["path"] = data["path"]
    if "resourceMethods" in data:
        import capo_api_gateway.types.map_of_method

        out["resource_methods"] = capo_api_gateway.types.map_of_method.deserialize_json(
            data["resourceMethods"]
        )
    return out
