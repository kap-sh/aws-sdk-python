"""Generated from Smithy shape ``com.amazonaws.clouddirectory#UpdateFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.facet_attribute_update_list
    import aws_sdk_clouddirectory.types.facet_name
    import aws_sdk_clouddirectory.types.object_type


class UpdateFacetRequest(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>"""
    name: "aws_sdk_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet.</p>"""
    attribute_updates: NotRequired[
        "aws_sdk_clouddirectory.types.facet_attribute_update_list.FacetAttributeUpdateList"
    ]
    """<p>List of attributes that need to be updated in a given schema <a>Facet</a>. Each attribute is followed by <code>AttributeAction</code>, which specifies the type of update operation to perform. </p>"""
    object_type: NotRequired["aws_sdk_clouddirectory.types.object_type.ObjectType"]
    """<p>The object type that is associated with the facet. See <a>CreateFacetRequest$ObjectType</a> for more details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "attribute_updates" in value:
        import aws_sdk_clouddirectory.types.facet_attribute_update_list

        out["AttributeUpdates"] = (
            aws_sdk_clouddirectory.types.facet_attribute_update_list.serialize_json(
                value["attribute_updates"]
            )
        )
    if "object_type" in value:
        import aws_sdk_clouddirectory.types.object_type

        out["ObjectType"] = aws_sdk_clouddirectory.types.object_type.serialize_json(
            value["object_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFacetRequest:
    out: UpdateFacetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateFacetRequest.name required")
    if "AttributeUpdates" in data:
        import aws_sdk_clouddirectory.types.facet_attribute_update_list

        out["attribute_updates"] = (
            aws_sdk_clouddirectory.types.facet_attribute_update_list.deserialize_json(
                data["AttributeUpdates"]
            )
        )
    if "ObjectType" in data:
        import aws_sdk_clouddirectory.types.object_type

        out["object_type"] = aws_sdk_clouddirectory.types.object_type.deserialize_json(
            data["ObjectType"]
        )
    return out
