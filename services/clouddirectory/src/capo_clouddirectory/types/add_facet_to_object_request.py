"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AddFacetToObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.attribute_key_and_value_list
    import capo_clouddirectory.types.object_reference
    import capo_clouddirectory.types.schema_facet


class AddFacetToObjectRequest(TypedDict, closed=True):
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    schema_facet: "capo_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Identifiers for the facet that you are adding to the object. See <a>SchemaFacet</a> for details.</p>"""
    object_attribute_list: NotRequired[
        "capo_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>Attributes on the facet that you are adding to the object.</p>"""
    object_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object you are adding the specified facet to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFacetToObjectRequest) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.schema_facet

    out["SchemaFacet"] = capo_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    if "object_attribute_list" in value:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["ObjectAttributeList"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["object_attribute_list"]
            )
        )
    import capo_clouddirectory.types.object_reference

    out["ObjectReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["object_reference"]
    )
    return out


def deserialize_json(data: dict) -> AddFacetToObjectRequest:
    out: AddFacetToObjectRequest = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import capo_clouddirectory.types.schema_facet

        out["schema_facet"] = capo_clouddirectory.types.schema_facet.deserialize_json(
            data["SchemaFacet"]
        )
    else:
        raise DeserializationError("AddFacetToObjectRequest.schema_facet required")
    if "ObjectAttributeList" in data:
        import capo_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            capo_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    if "ObjectReference" in data:
        import capo_clouddirectory.types.object_reference

        out["object_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("AddFacetToObjectRequest.object_reference required")
    return out
