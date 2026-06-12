"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AddFacetToObjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.schema_facet


class AddFacetToObjectRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> where the object resides. For more information, see <a>arns</a>.</p>"""
    schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Identifiers for the facet that you are adding to the object. See <a>SchemaFacet</a> for details.</p>"""
    object_attribute_list: NotRequired[
        "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    ]
    """<p>Attributes on the facet that you are adding to the object.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object you are adding the specified facet to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddFacetToObjectRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.schema_facet

    out["SchemaFacet"] = aws_sdk_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    if "object_attribute_list" in value:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["ObjectAttributeList"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.serialize_json(
                value["object_attribute_list"]
            )
        )
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddFacetToObjectRequest:
    out: AddFacetToObjectRequest = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import aws_sdk_clouddirectory.types.schema_facet

        out["schema_facet"] = (
            aws_sdk_clouddirectory.types.schema_facet.deserialize_json(
                data["SchemaFacet"]
            )
        )
    else:
        raise DeserializationError("AddFacetToObjectRequest.schema_facet required")
    if "ObjectAttributeList" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("AddFacetToObjectRequest.object_reference required")
    return out
