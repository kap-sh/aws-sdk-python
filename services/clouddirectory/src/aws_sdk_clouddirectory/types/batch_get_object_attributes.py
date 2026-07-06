"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchGetObjectAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name_list
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.schema_facet


class BatchGetObjectAttributes(TypedDict, closed=True):
    object_reference: "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    """<p>Reference that identifies the object whose attributes will be retrieved.</p>"""
    schema_facet: "aws_sdk_clouddirectory.types.schema_facet.SchemaFacet"
    """<p>Identifier for the facet whose attributes will be retrieved. See <a>SchemaFacet</a> for details.</p>"""
    attribute_names: (
        "aws_sdk_clouddirectory.types.attribute_name_list.AttributeNameList"
    )
    """<p>List of attribute names whose values will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetObjectAttributes) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.object_reference

    out["ObjectReference"] = (
        aws_sdk_clouddirectory.types.object_reference.serialize_json(
            value["object_reference"]
        )
    )
    import aws_sdk_clouddirectory.types.schema_facet

    out["SchemaFacet"] = aws_sdk_clouddirectory.types.schema_facet.serialize_json(
        value["schema_facet"]
    )
    import aws_sdk_clouddirectory.types.attribute_name_list

    out["AttributeNames"] = (
        aws_sdk_clouddirectory.types.attribute_name_list.serialize_json(
            value["attribute_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetObjectAttributes:
    out: BatchGetObjectAttributes = {}  # type: ignore[typeddict-item]
    if "ObjectReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["object_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ObjectReference"]
            )
        )
    else:
        raise DeserializationError("BatchGetObjectAttributes.object_reference required")
    if "SchemaFacet" in data:
        import aws_sdk_clouddirectory.types.schema_facet

        out["schema_facet"] = (
            aws_sdk_clouddirectory.types.schema_facet.deserialize_json(
                data["SchemaFacet"]
            )
        )
    else:
        raise DeserializationError("BatchGetObjectAttributes.schema_facet required")
    if "AttributeNames" in data:
        import aws_sdk_clouddirectory.types.attribute_name_list

        out["attribute_names"] = (
            aws_sdk_clouddirectory.types.attribute_name_list.deserialize_json(
                data["AttributeNames"]
            )
        )
    else:
        raise DeserializationError("BatchGetObjectAttributes.attribute_names required")
    return out
