"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Facet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.facet_name
    import aws_sdk_clouddirectory.types.facet_style
    import aws_sdk_clouddirectory.types.object_type


class Facet(TypedDict, closed=True):
    name: NotRequired["aws_sdk_clouddirectory.types.facet_name.FacetName"]
    """<p>The name of the <a>Facet</a>.</p>"""
    object_type: NotRequired["aws_sdk_clouddirectory.types.object_type.ObjectType"]
    """<p>The object type that is associated with the facet. See <a>CreateFacetRequest$ObjectType</a> for more details.</p>"""
    facet_style: NotRequired["aws_sdk_clouddirectory.types.facet_style.FacetStyle"]
    """<p>There are two different styles that you can define on any given facet, <code>Static</code> and <code>Dynamic</code>. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Facet) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "object_type" in value:
        import aws_sdk_clouddirectory.types.object_type

        out["ObjectType"] = aws_sdk_clouddirectory.types.object_type.serialize_json(
            value["object_type"]
        )
    if "facet_style" in value:
        import aws_sdk_clouddirectory.types.facet_style

        out["FacetStyle"] = aws_sdk_clouddirectory.types.facet_style.serialize_json(
            value["facet_style"]
        )
    return out


def deserialize_json(data: dict) -> Facet:
    out: Facet = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ObjectType" in data:
        import aws_sdk_clouddirectory.types.object_type

        out["object_type"] = aws_sdk_clouddirectory.types.object_type.deserialize_json(
            data["ObjectType"]
        )
    if "FacetStyle" in data:
        import aws_sdk_clouddirectory.types.facet_style

        out["facet_style"] = aws_sdk_clouddirectory.types.facet_style.deserialize_json(
            data["FacetStyle"]
        )
    return out
