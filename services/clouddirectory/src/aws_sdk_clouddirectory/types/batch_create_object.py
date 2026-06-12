"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchCreateObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list
    import aws_sdk_clouddirectory.types.batch_reference_name
    import aws_sdk_clouddirectory.types.link_name
    import aws_sdk_clouddirectory.types.object_reference
    import aws_sdk_clouddirectory.types.schema_facet_list


class BatchCreateObject(TypedDict):
    schema_facet: "aws_sdk_clouddirectory.types.schema_facet_list.SchemaFacetList"
    """<p>A list of <code>FacetArns</code> that will be associated with the object. For more information, see <a>arns</a>.</p>"""
    object_attribute_list: "aws_sdk_clouddirectory.types.attribute_key_and_value_list.AttributeKeyAndValueList"
    """<p>An attribute map, which contains an attribute ARN as the key and attribute value as the map value.</p>"""
    parent_reference: NotRequired[
        "aws_sdk_clouddirectory.types.object_reference.ObjectReference"
    ]
    """<p>If specified, the parent reference to which this object will be attached.</p>"""
    link_name: NotRequired["aws_sdk_clouddirectory.types.link_name.LinkName"]
    """<p>The name of the link.</p>"""
    batch_reference_name: NotRequired[
        "aws_sdk_clouddirectory.types.batch_reference_name.BatchReferenceName"
    ]
    """<p>The batch reference name. See <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/transaction_support.html\">Transaction Support</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateObject) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.schema_facet_list

    out["SchemaFacet"] = aws_sdk_clouddirectory.types.schema_facet_list.serialize_json(
        value["schema_facet"]
    )
    import aws_sdk_clouddirectory.types.attribute_key_and_value_list

    out["ObjectAttributeList"] = (
        aws_sdk_clouddirectory.types.attribute_key_and_value_list.serialize_json(
            value["object_attribute_list"]
        )
    )
    if "parent_reference" in value:
        import aws_sdk_clouddirectory.types.object_reference

        out["ParentReference"] = (
            aws_sdk_clouddirectory.types.object_reference.serialize_json(
                value["parent_reference"]
            )
        )
    if "link_name" in value:
        out["LinkName"] = value["link_name"]
    if "batch_reference_name" in value:
        out["BatchReferenceName"] = value["batch_reference_name"]
    return out


def deserialize_json(data: dict) -> BatchCreateObject:
    out: BatchCreateObject = {}  # type: ignore[typeddict-item]
    if "SchemaFacet" in data:
        import aws_sdk_clouddirectory.types.schema_facet_list

        out["schema_facet"] = (
            aws_sdk_clouddirectory.types.schema_facet_list.deserialize_json(
                data["SchemaFacet"]
            )
        )
    else:
        raise DeserializationError("BatchCreateObject.schema_facet required")
    if "ObjectAttributeList" in data:
        import aws_sdk_clouddirectory.types.attribute_key_and_value_list

        out["object_attribute_list"] = (
            aws_sdk_clouddirectory.types.attribute_key_and_value_list.deserialize_json(
                data["ObjectAttributeList"]
            )
        )
    else:
        raise DeserializationError("BatchCreateObject.object_attribute_list required")
    if "ParentReference" in data:
        import aws_sdk_clouddirectory.types.object_reference

        out["parent_reference"] = (
            aws_sdk_clouddirectory.types.object_reference.deserialize_json(
                data["ParentReference"]
            )
        )
    if "LinkName" in data:
        out["link_name"] = data["LinkName"]
    if "BatchReferenceName" in data:
        out["batch_reference_name"] = data["BatchReferenceName"]
    return out
