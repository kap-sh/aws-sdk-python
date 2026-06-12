"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAddFacetToObject``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.schema_facet


class BatchAddFacetToObject(TypedDict):
    schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Represents the facet being added to the object.</p>"""
    object_attribute_list: "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    """<p>The attributes to set on the object.</p>"""
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>A reference to the object being mutated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAddFacetToObject) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.schema_facet

    out["SchemaFacet"] = aws_sdk_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
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


def deserialize_json(data: dict) -> BatchAddFacetToObject:
    out: BatchAddFacetToObject = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import aws_sdk_clouddirectory.types.schema_facet

        out["schema_facet"] = (
            aws_sdk_clouddirectory.types.schema_facet.deserialize_json(
                data["SchemaFacet"]
            )
        )
    else:
        raise DeserializationError("BatchAddFacetToObject.schema_facet required")
    if "ObjectAttributeList" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAddFacetToObject.object_attribute_list required"
        )
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchAddFacetToObject.object_reference required")
    return out
